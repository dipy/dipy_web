.. AUTO-GENERATED FILE -- DO NOT EDIT!

:mod:`align`
============
.. automodule:: dipy.align

.. currentmodule:: dipy.align
.. autosummary::

   Bunch
   floating

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.imaffine`
-----------------------------
.. automodule:: dipy.align.imaffine

.. currentmodule:: dipy.align.imaffine
.. autosummary::

   AffineInversionError
   AffineMap
   AffineRegistration
   IsotropicScaleSpace
   MutualInformationMetric
   Optimizer
   ParzenJointHistogram
   ScaleSpace
   align_centers_of_mass
   align_geometric_centers
   align_origins
   compute_parzen_mi
   get_direction_and_spacings
   sample_domain_regular
   transform_centers_of_mass
   transform_geometric_centers
   transform_origins
   warn

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.imwarp`
---------------------------
.. automodule:: dipy.align.imwarp

.. currentmodule:: dipy.align.imwarp
.. autosummary::

   Bunch
   DiffeomorphicMap
   DiffeomorphicRegistration
   ScaleSpace
   SymmetricDiffeomorphicRegistration
   floating
   get_direction_and_spacings
   mult_aff
   with_metaclass

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.metrics`
----------------------------
.. automodule:: dipy.align.metrics

.. currentmodule:: dipy.align.metrics
.. autosummary::

   CCMetric
   EMMetric
   SSDMetric
   SimilarityMetric
   floating
   gradient
   v_cycle_2d
   v_cycle_3d
   with_metaclass

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.reslice`
----------------------------
.. automodule:: dipy.align.reslice

.. currentmodule:: dipy.align.reslice
.. autosummary::

   Pool
   affine_transform
   cpu_count
   reslice

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.scalespace`
-------------------------------
.. automodule:: dipy.align.scalespace

.. currentmodule:: dipy.align.scalespace
.. autosummary::

   IsotropicScaleSpace
   ScaleSpace
   floating

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`align.streamlinear`
---------------------------------
.. automodule:: dipy.align.streamlinear

.. currentmodule:: dipy.align.streamlinear
.. autosummary::

   BundleMinDistanceMatrixMetric
   BundleMinDistanceMetric
   BundleSumDistanceMatrixMetric
   Optimizer
   StreamlineDistanceMetric
   StreamlineLinearRegistration
   StreamlineRegistrationMap
   bundle_min_distance
   bundle_min_distance_fast
   bundle_sum_distance
   center_streamlines
   compose_matrix
   compose_matrix44
   compose_transformations
   decompose_matrix
   decompose_matrix44
   distance_matrix_mdf
   transform_streamlines
   unlist_streamlines
   with_metaclass


.. currentmodule:: dipy.align


:class:`Bunch`
~~~~~~~~~~~~~~


.. autoclass:: Bunch
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`floating`
~~~~~~~~~~~~~~~~~


.. autoclass:: floating
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


.. currentmodule:: dipy.align.imaffine


:class:`AffineInversionError`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: AffineInversionError
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`AffineMap`
~~~~~~~~~~~~~~~~~~


.. autoclass:: AffineMap
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`AffineRegistration`
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: AffineRegistration
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`IsotropicScaleSpace`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: IsotropicScaleSpace
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`MutualInformationMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: MutualInformationMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`Optimizer`
~~~~~~~~~~~~~~~~~~


.. autoclass:: Optimizer
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ParzenJointHistogram`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: ParzenJointHistogram
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ScaleSpace`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: ScaleSpace
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

align_centers_of_mass
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: align_centers_of_mass

align_geometric_centers
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: align_geometric_centers

align_origins
~~~~~~~~~~~~~

.. autofunction:: align_origins

compute_parzen_mi
~~~~~~~~~~~~~~~~~

.. autofunction:: compute_parzen_mi

get_direction_and_spacings
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: get_direction_and_spacings

sample_domain_regular
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: sample_domain_regular

transform_centers_of_mass
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_centers_of_mass

transform_geometric_centers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_geometric_centers

transform_origins
~~~~~~~~~~~~~~~~~

.. autofunction:: transform_origins

warn
~~~~

.. autofunction:: warn


.. currentmodule:: dipy.align.imwarp


:class:`Bunch`
~~~~~~~~~~~~~~


.. autoclass:: Bunch
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`DiffeomorphicMap`
~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: DiffeomorphicMap
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`DiffeomorphicRegistration`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: DiffeomorphicRegistration
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ScaleSpace`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: ScaleSpace
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`SymmetricDiffeomorphicRegistration`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: SymmetricDiffeomorphicRegistration
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`floating`
~~~~~~~~~~~~~~~~~


.. autoclass:: floating
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

get_direction_and_spacings
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: get_direction_and_spacings

mult_aff
~~~~~~~~

.. autofunction:: mult_aff

with_metaclass
~~~~~~~~~~~~~~

.. autofunction:: with_metaclass


.. currentmodule:: dipy.align.metrics


:class:`CCMetric`
~~~~~~~~~~~~~~~~~


.. autoclass:: CCMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`EMMetric`
~~~~~~~~~~~~~~~~~


.. autoclass:: EMMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`SSDMetric`
~~~~~~~~~~~~~~~~~~


.. autoclass:: SSDMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`SimilarityMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: SimilarityMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`floating`
~~~~~~~~~~~~~~~~~


.. autoclass:: floating
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

gradient
~~~~~~~~

.. autofunction:: gradient

v_cycle_2d
~~~~~~~~~~

.. autofunction:: v_cycle_2d

v_cycle_3d
~~~~~~~~~~

.. autofunction:: v_cycle_3d

with_metaclass
~~~~~~~~~~~~~~

.. autofunction:: with_metaclass


.. currentmodule:: dipy.align.reslice

Pool
~~~~

.. autofunction:: Pool

affine_transform
~~~~~~~~~~~~~~~~

.. autofunction:: affine_transform

cpu_count
~~~~~~~~~

.. autofunction:: cpu_count

reslice
~~~~~~~

.. autofunction:: reslice


.. currentmodule:: dipy.align.scalespace


:class:`IsotropicScaleSpace`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: IsotropicScaleSpace
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ScaleSpace`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: ScaleSpace
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`floating`
~~~~~~~~~~~~~~~~~


.. autoclass:: floating
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


.. currentmodule:: dipy.align.streamlinear


:class:`BundleMinDistanceMatrixMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: BundleMinDistanceMatrixMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`BundleMinDistanceMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: BundleMinDistanceMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`BundleSumDistanceMatrixMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: BundleSumDistanceMatrixMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`Optimizer`
~~~~~~~~~~~~~~~~~~


.. autoclass:: Optimizer
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`StreamlineDistanceMetric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: StreamlineDistanceMetric
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`StreamlineLinearRegistration`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: StreamlineLinearRegistration
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`StreamlineRegistrationMap`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: StreamlineRegistrationMap
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

bundle_min_distance
~~~~~~~~~~~~~~~~~~~

.. autofunction:: bundle_min_distance

bundle_min_distance_fast
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: bundle_min_distance_fast

bundle_sum_distance
~~~~~~~~~~~~~~~~~~~

.. autofunction:: bundle_sum_distance

center_streamlines
~~~~~~~~~~~~~~~~~~

.. autofunction:: center_streamlines

compose_matrix
~~~~~~~~~~~~~~

.. autofunction:: compose_matrix

compose_matrix44
~~~~~~~~~~~~~~~~

.. autofunction:: compose_matrix44

compose_transformations
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compose_transformations

decompose_matrix
~~~~~~~~~~~~~~~~

.. autofunction:: decompose_matrix

decompose_matrix44
~~~~~~~~~~~~~~~~~~

.. autofunction:: decompose_matrix44

distance_matrix_mdf
~~~~~~~~~~~~~~~~~~~

.. autofunction:: distance_matrix_mdf

transform_streamlines
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_streamlines

unlist_streamlines
~~~~~~~~~~~~~~~~~~

.. autofunction:: unlist_streamlines

with_metaclass
~~~~~~~~~~~~~~

.. autofunction:: with_metaclass

