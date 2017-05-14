.. AUTO-GENERATED FILE -- DO NOT EDIT!

:mod:`core`
===========
.. automodule:: dipy.core

.. currentmodule:: dipy.core
.. autosummary::

   test

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.geometry`
----------------------------
.. automodule:: dipy.core.geometry

.. currentmodule:: dipy.core.geometry
.. autosummary::

   cart2sphere
   cart_distance
   circumradius
   compose_matrix
   compose_transformations
   decompose_matrix
   dist_to_corner
   euler_matrix
   lambert_equal_area_projection_cart
   lambert_equal_area_projection_polar
   nearest_pos_semi_def
   normalized_vector
   perpendicular_directions
   rodrigues_axis_rotation
   sph2latlon
   sphere2cart
   sphere_distance
   vec2vec_rotmat
   vector_cosine
   vector_norm

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.gradients`
-----------------------------
.. automodule:: dipy.core.gradients

.. currentmodule:: dipy.core.gradients
.. autosummary::

   GradientTable
   auto_attr
   gradient_table
   gradient_table_from_bvals_bvecs
   inv
   polar
   reorient_bvecs
   vector_norm

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.graph`
-------------------------
.. automodule:: dipy.core.graph

.. currentmodule:: dipy.core.graph
.. autosummary::

   Graph

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.histeq`
--------------------------
.. automodule:: dipy.core.histeq

.. currentmodule:: dipy.core.histeq
.. autosummary::

   histeq

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.ndindex`
---------------------------
.. automodule:: dipy.core.ndindex

.. currentmodule:: dipy.core.ndindex
.. autosummary::

   as_strided
   ndindex

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.onetime`
---------------------------
.. automodule:: dipy.core.onetime

.. currentmodule:: dipy.core.onetime
.. autosummary::

   OneTimeProperty
   ResetMixin
   auto_attr
   setattr_on_read

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.optimize`
----------------------------
.. automodule:: dipy.core.optimize

.. currentmodule:: dipy.core.optimize
.. autosummary::

   LooseVersion
   NonNegativeLeastSquares
   Optimizer
   SKLearnLinearSolver
   minimize
   sparse_nnls
   spdot
   with_metaclass

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.profile`
---------------------------
.. automodule:: dipy.core.profile

.. currentmodule:: dipy.core.profile
.. autosummary::

   Profiler
   optional_package

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.rng`
-----------------------
.. automodule:: dipy.core.rng

.. currentmodule:: dipy.core.rng
.. autosummary::

   LEcuyer
   WichmannHill1982
   WichmannHill2006
   architecture
   floor

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.sphere`
--------------------------
.. automodule:: dipy.core.sphere

.. currentmodule:: dipy.core.sphere
.. autosummary::

   HemiSphere
   Sphere
   xrange
   auto_attr
   cart2sphere
   disperse_charges
   euler_characteristic_check
   faces_from_sphere_vertices
   interp_rbf
   remove_similar_vertices
   sphere2cart
   unique_edges
   unique_sets
   vector_norm

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.sphere_stats`
--------------------------------
.. automodule:: dipy.core.sphere_stats

.. currentmodule:: dipy.core.sphere_stats
.. autosummary::

   permutations
   angular_similarity
   compare_orientation_sets
   eigenstats
   random_uniform_on_sphere

.. AUTO-GENERATED FILE -- DO NOT EDIT!

Module: :mod:`core.subdivide_octahedron`
----------------------------------------
.. automodule:: dipy.core.subdivide_octahedron

.. currentmodule:: dipy.core.subdivide_octahedron
.. autosummary::

   HemiSphere
   create_unit_hemisphere
   create_unit_sphere


.. currentmodule:: dipy.core

test
~~~~

.. autofunction:: test


.. currentmodule:: dipy.core.geometry

cart2sphere
~~~~~~~~~~~

.. autofunction:: cart2sphere

cart_distance
~~~~~~~~~~~~~

.. autofunction:: cart_distance

circumradius
~~~~~~~~~~~~

.. autofunction:: circumradius

compose_matrix
~~~~~~~~~~~~~~

.. autofunction:: compose_matrix

compose_transformations
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compose_transformations

decompose_matrix
~~~~~~~~~~~~~~~~

.. autofunction:: decompose_matrix

dist_to_corner
~~~~~~~~~~~~~~

.. autofunction:: dist_to_corner

euler_matrix
~~~~~~~~~~~~

.. autofunction:: euler_matrix

lambert_equal_area_projection_cart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: lambert_equal_area_projection_cart

lambert_equal_area_projection_polar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: lambert_equal_area_projection_polar

nearest_pos_semi_def
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: nearest_pos_semi_def

normalized_vector
~~~~~~~~~~~~~~~~~

.. autofunction:: normalized_vector

perpendicular_directions
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: perpendicular_directions

rodrigues_axis_rotation
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: rodrigues_axis_rotation

sph2latlon
~~~~~~~~~~

.. autofunction:: sph2latlon

sphere2cart
~~~~~~~~~~~

.. autofunction:: sphere2cart

sphere_distance
~~~~~~~~~~~~~~~

.. autofunction:: sphere_distance

vec2vec_rotmat
~~~~~~~~~~~~~~

.. autofunction:: vec2vec_rotmat

vector_cosine
~~~~~~~~~~~~~

.. autofunction:: vector_cosine

vector_norm
~~~~~~~~~~~

.. autofunction:: vector_norm


.. currentmodule:: dipy.core.gradients


:class:`GradientTable`
~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: GradientTable
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

auto_attr
~~~~~~~~~

.. autofunction:: auto_attr

gradient_table
~~~~~~~~~~~~~~

.. autofunction:: gradient_table

gradient_table_from_bvals_bvecs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: gradient_table_from_bvals_bvecs

inv
~~~

.. autofunction:: inv

polar
~~~~~

.. autofunction:: polar

reorient_bvecs
~~~~~~~~~~~~~~

.. autofunction:: reorient_bvecs

vector_norm
~~~~~~~~~~~

.. autofunction:: vector_norm


.. currentmodule:: dipy.core.graph


:class:`Graph`
~~~~~~~~~~~~~~


.. autoclass:: Graph
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


.. currentmodule:: dipy.core.histeq

histeq
~~~~~~

.. autofunction:: histeq


.. currentmodule:: dipy.core.ndindex

as_strided
~~~~~~~~~~

.. autofunction:: as_strided

ndindex
~~~~~~~

.. autofunction:: ndindex


.. currentmodule:: dipy.core.onetime


:class:`OneTimeProperty`
~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: OneTimeProperty
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`ResetMixin`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: ResetMixin
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

auto_attr
~~~~~~~~~

.. autofunction:: auto_attr

setattr_on_read
~~~~~~~~~~~~~~~

.. autofunction:: setattr_on_read


.. currentmodule:: dipy.core.optimize


:class:`LooseVersion`
~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: LooseVersion
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`NonNegativeLeastSquares`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: NonNegativeLeastSquares
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


:class:`SKLearnLinearSolver`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: SKLearnLinearSolver
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

minimize
~~~~~~~~

.. autofunction:: minimize

sparse_nnls
~~~~~~~~~~~

.. autofunction:: sparse_nnls

spdot
~~~~~

.. autofunction:: spdot

with_metaclass
~~~~~~~~~~~~~~

.. autofunction:: with_metaclass


.. currentmodule:: dipy.core.profile


:class:`Profiler`
~~~~~~~~~~~~~~~~~


.. autoclass:: Profiler
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

optional_package
~~~~~~~~~~~~~~~~

.. autofunction:: optional_package


.. currentmodule:: dipy.core.rng

LEcuyer
~~~~~~~

.. autofunction:: LEcuyer

WichmannHill1982
~~~~~~~~~~~~~~~~

.. autofunction:: WichmannHill1982

WichmannHill2006
~~~~~~~~~~~~~~~~

.. autofunction:: WichmannHill2006

architecture
~~~~~~~~~~~~

.. autofunction:: architecture

floor
~~~~~

.. autofunction:: floor


.. currentmodule:: dipy.core.sphere


:class:`HemiSphere`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: HemiSphere
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__


:class:`Sphere`
~~~~~~~~~~~~~~~


.. autoclass:: Sphere
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

auto_attr
~~~~~~~~~

.. autofunction:: auto_attr

cart2sphere
~~~~~~~~~~~

.. autofunction:: cart2sphere

disperse_charges
~~~~~~~~~~~~~~~~

.. autofunction:: disperse_charges

euler_characteristic_check
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: euler_characteristic_check

faces_from_sphere_vertices
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: faces_from_sphere_vertices

interp_rbf
~~~~~~~~~~

.. autofunction:: interp_rbf

remove_similar_vertices
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: remove_similar_vertices

sphere2cart
~~~~~~~~~~~

.. autofunction:: sphere2cart

unique_edges
~~~~~~~~~~~~

.. autofunction:: unique_edges

unique_sets
~~~~~~~~~~~

.. autofunction:: unique_sets

vector_norm
~~~~~~~~~~~

.. autofunction:: vector_norm


.. currentmodule:: dipy.core.sphere_stats


:class:`permutations`
~~~~~~~~~~~~~~~~~~~~~


.. autoclass:: permutations
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

angular_similarity
~~~~~~~~~~~~~~~~~~

.. autofunction:: angular_similarity

compare_orientation_sets
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: compare_orientation_sets

eigenstats
~~~~~~~~~~

.. autofunction:: eigenstats

random_uniform_on_sphere
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: random_uniform_on_sphere


.. currentmodule:: dipy.core.subdivide_octahedron


:class:`HemiSphere`
~~~~~~~~~~~~~~~~~~~


.. autoclass:: HemiSphere
  :members:
  :undoc-members:
  :show-inheritance:

  .. automethod:: __init__

create_unit_hemisphere
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: create_unit_hemisphere

create_unit_sphere
~~~~~~~~~~~~~~~~~~

.. autofunction:: create_unit_sphere

