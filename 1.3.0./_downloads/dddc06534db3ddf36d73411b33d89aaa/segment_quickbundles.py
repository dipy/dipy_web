"""
=========================================
Tractography Clustering with QuickBundles
=========================================

This example explains how we can use QuickBundles [Garyfallidis12]_ to
simplify/cluster streamlines.

First import the necessary modules.
"""

import numpy as np
from dipy.io.streamline import load_tractogram
from dipy.segment.clustering import QuickBundles
from dipy.io.pickles import save_pickle
from dipy.data import get_fnames
from dipy.viz import window, actor

###############################################################################
# For educational purposes we will try to cluster a small streamline bundle
# known from neuroanatomy as the fornix.

fname = get_fnames('fornix')

###############################################################################
# Load fornix streamlines.

fornix = load_tractogram(fname, 'same', bbox_valid_check=False)
streamlines = fornix.streamlines

###############################################################################
# Perform QuickBundles clustering using the MDF metric and a 10mm distance
# threshold. Keep in mind that since the MDF metric requires streamlines to
# have the same number of points, the clustering algorithm will internally use
# a representation of streamlines that have been automatically
# downsampled/upsampled so they have only 12 points (To set manually the number
# of points, see :ref:`clustering-examples-ResampleFeature`).

qb = QuickBundles(threshold=10.)
clusters = qb.cluster(streamlines)

###############################################################################
# `clusters` is a `ClusterMap` object which contains attributes that
# provide information about the clustering result.

print("Nb. clusters:", len(clusters))
print("Cluster sizes:", map(len, clusters))
print("Small clusters:", clusters < 10)
print("Streamlines indices of the first cluster:\n", clusters[0].indices)
print("Centroid of the last cluster:\n", clusters[-1].centroid)

###############################################################################
# `clusters` has also attributes like `centroids` (cluster representatives),
# and methods like `add`, `remove`, and `clear` to modify the clustering
# result.
#
# Lets first show the initial dataset.

# Enables/disables interactive visualization
interactive = False

scene = window.Scene()
scene.SetBackground(1, 1, 1)
scene.add(actor.streamtube(streamlines, window.colors.white))
window.record(scene, out_path='fornix_initial.png', size=(600, 600))
if interactive:
    window.show(scene)

###############################################################################
# .. figure:: fornix_initial.png
#    :align: center
#
#    Initial Fornix dataset.
#
# Show the centroids of the fornix after clustering (with random colors):

colormap = actor.create_colormap(np.arange(len(clusters)))

scene.clear()
scene.SetBackground(1, 1, 1)
scene.add(actor.streamtube(streamlines, window.colors.white, opacity=0.05))
scene.add(actor.streamtube(clusters.centroids, colormap, linewidth=0.4))
window.record(scene, out_path='fornix_centroids.png', size=(600, 600))
if interactive:
    window.show(scene)

###############################################################################
# .. figure:: fornix_centroids.png
#    :align: center
#
#    Showing the different QuickBundles centroids with random colors.
#
# Show the labeled fornix (colors from centroids).

colormap_full = np.ones((len(streamlines), 3))
for cluster, color in zip(clusters, colormap):
    colormap_full[cluster.indices] = color

scene.clear()
scene.SetBackground(1, 1, 1)
scene.add(actor.streamtube(streamlines, colormap_full))
window.record(scene, out_path='fornix_clusters.png', size=(600, 600))
if interactive:
    window.show(scene)

###############################################################################
# .. figure:: fornix_clusters.png
#    :align: center
#
#    Showing the different clusters.
#
# It is also possible to save the complete `ClusterMap` object with pickling.

save_pickle('QB.pkl', clusters)

###############################################################################
# Finally, here is a video of QuickBundles applied on a larger dataset.
#
# .. raw:: html
#
#     <iframe width="420" height="315" src="http://www.youtube.com/embed/kstL7KKqu94" frameborder="0" allowfullscreen></iframe>
#
# .. include:: ../links_names.inc
#
# References
# ----------
#
# .. [Garyfallidis12] Garyfallidis E. et al., QuickBundles a method for
#                     tractography simplification, Frontiers in Neuroscience,
#                     vol 6, no 175, 2012.
