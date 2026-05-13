Overview
========

``coresg-graphhdbscan`` is a Python package for density-based clustering on similarity graphs derived from feature-vector data or directly provided by the user.

The package combines two main ideas:

1. construction of a weighted graph that reflects local similarity structure
2. application of a specialized CoreSG-HDBSCAN* pipeline designed to operate on graph data representations

This package is designed for settings where feature-vector representations are not suitable for clustering, such as Euclidean geometry in very high-dimensional spaces, where clustering should instead be guided by a learned or hand-crafted similarity graph as an intrinsically lower-dimensional representation of the data.


Main features
-------------

The package currently supports the following capabilities:

- graph-based clustering through ``GraphCoreSGHDBSCAN``
- multiple ``min_samples`` values in a single model run
- three graph-construction backends plus a precomputed graph mode
- three metric modes: ``euclidean``, ``cosine``, and ``hybrid_euclidean_cosine``
- optional relabeling of noise points by density-based label propagation
- compatibility with NetworkX graphs, dense adjacency matrices, and sparse adjacency matrices in precomputed mode
- access to HDBSCAN*-style outputs such as labels, probabilities, and condensed trees
- direct access to stored labels, condensed trees, and optional per-``m`` models

Package structure
-----------------

The package is centered around two public classes:

``CoreSGHDBSCAN``
   The lower-level CoreSG implementation operating on feature vectors or
   distance matrices.

``GraphCoreSGHDBSCAN``
   The graph-oriented wrapper that constructs a similarity graph, converts it to a
   weighted structutal dissimilarity graph, and then runs CoreSGHDBSCAN.

For most users, ``GraphCoreSGHDBSCAN`` is the main entry point.

When to use this package
------------------------

This package is especially useful when:

- you work with very high-dimensional data, and simple metrics like Euclidean distance alone is not the best description of local structure
- a similarity graph is more meaningful than a raw feature-space view
- you want to compare several ``min_samples`` values efficiently in one run
- you want HDBSCAN*-style hierarchical clustering behavior on top of a graph-based representation
- you already have a graph or adjacency matrix and want to cluster directly from it

Typical workflow
----------------

A typical graph-based clustering workflow in this package is:

1. construct or provide a similarity graph
2. convert it into a weighted structural similarity graph
3. convert similarity to dissimilarity
4. ensure graph connectivity
5. run CoreSGHDBSCAN for one or more ``min_samples`` values
6. inspect the condensed tree and choose a solution
7. optionally reassign noise points if ``no_noise=True``

Typical entry point
-------------------

For most users, the main entry point is:

.. code-block:: python

   from coresg_graphhdbscan import GraphCoreSGHDBSCAN

A simple starting example is:

.. code-block:: python

   from coresg_graphhdbscan import GraphCoreSGHDBSCAN

   model = GraphCoreSGHDBSCAN(
       min_samples=10,
       sim_graph_method="sc_umap",
       metric="euclidean",
       n_neighbors=15,
       no_noise=True,
       heuristic_connect=False,
   )

   model.fit(X)
   labels = model.fit_predict(X)

Stored results after fitting
----------------------------

After fitting, the package stores results for each tested
``min_samples`` value.

The main user-facing object is ``GraphCoreSGHDBSCAN``. Internally, it
runs a Core-SG engine across one or more ``min_samples`` values and
stores per-``m`` results.

The most important fitted result containers are:

- ``labels_by_m_``:
  dictionary mapping each fitted ``min_samples`` value to its stored
  cluster labels.
- ``condensed_trees_``:
  dictionary mapping each fitted ``min_samples`` value to its condensed
  tree object.
- ``models_``:
  dictionary mapping each fitted ``min_samples`` value to a saved model
  object when ``save_models=True``.

This makes it possible to inspect a fitted solution directly without
re-running the model.

Typical post-fit access looks like:

.. code-block:: python

   g.fit(X)

   labels_10 = g.labels_by_m_[10]
   tree_10 = g.condensed_trees_[10]

   # only available when save_models=True
   model_10 = g.models_[10]

Related pages
-------------

For more detail, see:

- :doc:`installation`
- :doc:`usage`
- :doc:`parameters`
- :doc:`api`
