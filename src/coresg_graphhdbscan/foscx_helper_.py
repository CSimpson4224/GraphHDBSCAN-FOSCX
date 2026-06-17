import numpy as np
from foscx import FOSCX

def get_clusters_foscx_(tree, foscx_settings):

    FOSCX_DEFAULTS = {"top_M":1,'density':True,'metric':'precomputed_similarity'}                      

    settings = {**FOSCX_DEFAULTS, **(foscx_settings or {})}

    fosc_model = FOSCX(**foscx_settings)
    fosc_model.fit(tree)
    clusters = fosc_model.candidate_nodes_

    def process_partition(partition_idx, cluster_nodes):
        probs = get_probabilities_(fosc_model.cluster_tree_, cluster_nodes)
        lbls = fosc_model.get_labels(partition_idx)
        quals = fosc_model.cluster_tree_.clusteval[cluster_nodes]
        return lbls, probs, quals

    # Single partition: flat list of ints
    if isinstance(clusters[0], int):
        lbls, probs, quals = process_partition(0, clusters)
        return lbls, probs, quals

    # Multiple partitions: list of lists
    labels, probabilities, qualities = [], [], []
    for i, cluster_nodes in enumerate(clusters):
        lbls, probs, quals = process_partition(i, cluster_nodes)
        labels.append(lbls)
        probabilities.append(probs)
        qualities.append(quals)
    return labels, probabilities, qualities


def get_probabilities_(fosc_tree,clusters):

    n = max(fosc_tree.sizes)

    probabilities = np.zeros(n)

    for cnode in clusters:

        max_lambda = np.max(fosc_tree.distance[fosc_tree.get_children(cnode)])

        for point in fosc_tree.get_node_indices(cnode):

            if max_lambda == 0 or not np.isfinite(fosc_tree.distance[point]):
                probabilities[point] = 1.0
            else:
                lambda_ = min(fosc_tree.distance[point],max_lambda)
                probabilities[point] = lambda_ / max_lambda

    return probabilities