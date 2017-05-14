.. AUTO-GENERATED FILE -- DO NOT EDIT!

:mod:`tracking`
===============
.. automodule:: dipy.tracking

.. currentmodule:: dipy.tracking
.. autosummary::

   bench
   test

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking._utils`
------------------------------
.. automodule:: dipy.tracking._utils

.. currentmodule:: dipy.tracking._utils
.. autosummary::

   warn

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.benchmarks`
----------------------------------
.. automodule:: dipy.tracking.benchmarks

.. currentmodule:: dipy.tracking.benchmarks
.. autosummary::


.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.benchmarks.bench_streamline`
---------------------------------------------------
.. automodule:: dipy.tracking.benchmarks.bench_streamline

.. currentmodule:: dipy.tracking.benchmarks.bench_streamline
.. autosummary::

   bench_compress_streamlines
   bench_length
   bench_set_number_of_points
   compress_streamlines
   compress_streamlines_python
   get_data
   length
   length_python
   measure
   set_number_of_points
   set_number_of_points_python

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.eudx`
----------------------------
.. automodule:: dipy.tracking.eudx

.. currentmodule:: dipy.tracking.eudx
.. autosummary::

   EuDX
   eudx_both_directions
   get_sphere

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.learning`
--------------------------------
.. automodule:: dipy.tracking.learning

.. currentmodule:: dipy.tracking.learning
.. autosummary::

   detect_corresponding_tracks
   detect_corresponding_tracks_plus

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.life`
----------------------------
.. automodule:: dipy.tracking.life

.. currentmodule:: dipy.tracking.life
.. autosummary::

   FiberFit
   FiberModel
   LifeSignalMaker
   ReconstFit
   ReconstModel
   range
   grad_tensor
   gradient
   streamline_gradients
   streamline_signal
   streamline_tensors
   transform_streamlines
   unique_rows
   voxel2streamline

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.local`
-----------------------------
.. automodule:: dipy.tracking.local

.. currentmodule:: dipy.tracking.local
.. autosummary::

   ActTissueClassifier
   BinaryTissueClassifier
   DirectionGetter
   LocalTracking
   ThresholdTissueClassifier
   TissueClassifier

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.local.localtracking`
-------------------------------------------
.. automodule:: dipy.tracking.local.localtracking

.. currentmodule:: dipy.tracking.local.localtracking
.. autosummary::

   Bunch
   LocalTracking
   local_tracker

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.markov`
------------------------------
.. automodule:: dipy.tracking.markov

.. currentmodule:: dipy.tracking.markov
.. autosummary::

   BoundaryStepper
   CDT_NNO
   ClosestDirectionTracker
   DirectionFinder
   FixedSizeStepper
   MarkovIntegrator
   NearestNeighborInterpolator
   OutsideImage
   ProbabilisticOdfWeightedTracker
   xrange
   markov_streamline
   peak_directions

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.metrics`
-------------------------------
.. automodule:: dipy.tracking.metrics

.. currentmodule:: dipy.tracking.metrics
.. autosummary::

   xrange
   arbitrarypoint
   bytes
   center_of_mass
   downsample
   endpoint
   frenet_serret
   generate_combinations
   inside_sphere
   inside_sphere_points
   intersect_sphere
   length
   longest_track_bundle
   magn
   mean_curvature
   mean_orientation
   midpoint
   midpoint2point
   principal_components
   splev
   spline
   splprep
   startpoint
   winding

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`tracking.streamline`
----------------------------------
.. automodule:: dipy.tracking.streamline

.. currentmodule:: dipy.tracking.streamline
.. autosummary::

   apply_affine
   cdist
   center_streamlines
   compress_streamlines
   deepcopy
   dist_to_corner
   length
   orient_by_rois
   relist_streamlines
   select_by_rois
   select_random_set_of_streamlines
   set_number_of_points
   streamline_near_roi
   transform_streamlines
   unlist_streamlines
   values_from_volume
   warn


.. currentmodule:: dipy.tracking

bench
~~~~~

.. autofunction:: bench

test
~~~~

.. autofunction:: test


.. currentmodule:: dipy.tracking._utils

warn
~~~~

.. autofunction:: warn


.. currentmodule:: dipy.tracking.benchmarks


.. currentmodule:: dipy.tracking.benchmarks.bench_streamline

bench_compress_streamlines
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: bench_compress_streamlines

bench_length
~~~~~~~~~~~~

.. autofunction:: bench_length

bench_set_number_of_points
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: bench_set_number_of_points

compress_streamlines
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compress_streamlines

compress_streamlines_python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compress_streamlines_python

get_data
~~~~~~~~

.. autofunction:: get_data

length
~~~~~~

.. autofunction:: length

length_python
~~~~~~~~~~~~~

.. autofunction:: length_python

measure
~~~~~~~

.. autofunction:: measure

set_number_of_points
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: set_number_of_points

set_number_of_points_python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: set_number_of_points_python


.. currentmodule:: dipy.tracking.eudx


:class:`EuDX`
~~~~~~~~~~~~~


.. autoclass:: EuDX
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

eudx_both_directions
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: eudx_both_directions

get_sphere
~~~~~~~~~~

.. autofunction:: get_sphere


.. currentmodule:: dipy.tracking.learning

detect_corresponding_tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: detect_corresponding_tracks

detect_corresponding_tracks_plus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: detect_corresponding_tracks_plus


.. currentmodule:: dipy.tracking.life


:class:`FiberFit`
~~~~~~~~~~~~~~~~~


.. autoclass:: FiberFit
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`FiberModel`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: FiberModel
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`LifeSignalMaker`
~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: LifeSignalMaker
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ReconstFit`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: ReconstFit
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ReconstModel`
~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ReconstModel
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`range`
~~~~~~~~~~~~~~


.. autoclass:: range
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

grad_tensor
~~~~~~~~~~~

.. autofunction:: grad_tensor

gradient
~~~~~~~~

.. autofunction:: gradient

streamline_gradients
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: streamline_gradients

streamline_signal
~~~~~~~~~~~~~~~~~

.. autofunction:: streamline_signal

streamline_tensors
~~~~~~~~~~~~~~~~~~

.. autofunction:: streamline_tensors

transform_streamlines
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_streamlines

unique_rows
~~~~~~~~~~~

.. autofunction:: unique_rows

voxel2streamline
~~~~~~~~~~~~~~~~

.. autofunction:: voxel2streamline


.. currentmodule:: dipy.tracking.local


:class:`ActTissueClassifier`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ActTissueClassifier
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`BinaryTissueClassifier`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: BinaryTissueClassifier
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`DirectionGetter`
~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: DirectionGetter
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`LocalTracking`
~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: LocalTracking
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ThresholdTissueClassifier`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ThresholdTissueClassifier
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`TissueClassifier`
~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: TissueClassifier
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


.. currentmodule:: dipy.tracking.local.localtracking


:class:`Bunch`
~~~~~~~~~~~~~~


.. autoclass:: Bunch
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`LocalTracking`
~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: LocalTracking
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

local_tracker
~~~~~~~~~~~~~

.. autofunction:: local_tracker


.. currentmodule:: dipy.tracking.markov


:class:`BoundaryStepper`
~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: BoundaryStepper
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`CDT_NNO`
~~~~~~~~~~~~~~~~


.. autoclass:: CDT_NNO
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ClosestDirectionTracker`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ClosestDirectionTracker
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`DirectionFinder`
~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: DirectionFinder
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`FixedSizeStepper`
~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: FixedSizeStepper
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`MarkovIntegrator`
~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: MarkovIntegrator
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`NearestNeighborInterpolator`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: NearestNeighborInterpolator
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`OutsideImage`
~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: OutsideImage
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ProbabilisticOdfWeightedTracker`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ProbabilisticOdfWeightedTracker
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`xrange`
~~~~~~~~~~~~~~~


.. autoclass:: xrange
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

markov_streamline
~~~~~~~~~~~~~~~~~

.. autofunction:: markov_streamline

peak_directions
~~~~~~~~~~~~~~~

.. autofunction:: peak_directions


.. currentmodule:: dipy.tracking.metrics


:class:`xrange`
~~~~~~~~~~~~~~~


.. autoclass:: xrange
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

arbitrarypoint
~~~~~~~~~~~~~~

.. autofunction:: arbitrarypoint

bytes
~~~~~

.. autofunction:: bytes

center_of_mass
~~~~~~~~~~~~~~

.. autofunction:: center_of_mass

downsample
~~~~~~~~~~

.. autofunction:: downsample

endpoint
~~~~~~~~

.. autofunction:: endpoint

frenet_serret
~~~~~~~~~~~~~

.. autofunction:: frenet_serret

generate_combinations
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generate_combinations

inside_sphere
~~~~~~~~~~~~~

.. autofunction:: inside_sphere

inside_sphere_points
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: inside_sphere_points

intersect_sphere
~~~~~~~~~~~~~~~~

.. autofunction:: intersect_sphere

length
~~~~~~

.. autofunction:: length

longest_track_bundle
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: longest_track_bundle

magn
~~~~

.. autofunction:: magn

mean_curvature
~~~~~~~~~~~~~~

.. autofunction:: mean_curvature

mean_orientation
~~~~~~~~~~~~~~~~

.. autofunction:: mean_orientation

midpoint
~~~~~~~~

.. autofunction:: midpoint

midpoint2point
~~~~~~~~~~~~~~

.. autofunction:: midpoint2point

principal_components
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: principal_components

splev
~~~~~

.. autofunction:: splev

spline
~~~~~~

.. autofunction:: spline

splprep
~~~~~~~

.. autofunction:: splprep

startpoint
~~~~~~~~~~

.. autofunction:: startpoint

winding
~~~~~~~

.. autofunction:: winding


.. currentmodule:: dipy.tracking.streamline

apply_affine
~~~~~~~~~~~~

.. autofunction:: apply_affine

cdist
~~~~~

.. autofunction:: cdist

center_streamlines
~~~~~~~~~~~~~~~~~~

.. autofunction:: center_streamlines

compress_streamlines
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compress_streamlines

deepcopy
~~~~~~~~

.. autofunction:: deepcopy

dist_to_corner
~~~~~~~~~~~~~~

.. autofunction:: dist_to_corner

length
~~~~~~

.. autofunction:: length

orient_by_rois
~~~~~~~~~~~~~~

.. autofunction:: orient_by_rois

relist_streamlines
~~~~~~~~~~~~~~~~~~

.. autofunction:: relist_streamlines

select_by_rois
~~~~~~~~~~~~~~

.. autofunction:: select_by_rois

select_random_set_of_streamlines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: select_random_set_of_streamlines

set_number_of_points
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: set_number_of_points

streamline_near_roi
~~~~~~~~~~~~~~~~~~~

.. autofunction:: streamline_near_roi

transform_streamlines
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_streamlines

unlist_streamlines
~~~~~~~~~~~~~~~~~~

.. autofunction:: unlist_streamlines

values_from_volume
~~~~~~~~~~~~~~~~~~

.. autofunction:: values_from_volume

warn
~~~~

.. autofunction:: warn

