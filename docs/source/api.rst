API reference
=============

This section documents the public API of ``coresg-graphhdbscan``.

Main public API
---------------

The most important user-facing class is ``GraphCoreSGHDBSCAN``.

Important public methods include:

- ``fit``
- ``fit_predict``
- ``labels_for``
- ``model``
- ``plot_condensed_tree``
- ``interactive_condensed_tree``

Important fitted result attributes include:

- ``models_``
- ``condensed_trees_``
- ``labels_by_m_``
- ``coresg_``
- ``dist_matrix_``
- ``similarity_graph_``
- ``connected_graph_``

Main classes
------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   coresg_graphhdbscan.graph.GraphCoreSGHDBSCAN
   coresg_graphhdbscan.core.CoreSGHDBSCAN
   coresg_graphhdbscan.core.CoreSGModel

Main utility function
---------------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   coresg_graphhdbscan.core.plot_condensed_tree_for_m

Module reference
----------------

Graph module
^^^^^^^^^^^^

.. automodule:: coresg_graphhdbscan.graph
   :members:
   :undoc-members:
   :show-inheritance:

Core module
^^^^^^^^^^^

.. automodule:: coresg_graphhdbscan.core
   :members:
   :undoc-members:
   :show-inheritance:

Metrics module
^^^^^^^^^^^^^^

.. automodule:: coresg_graphhdbscan.metrics
   :members:
   :undoc-members:
   :show-inheritance:
