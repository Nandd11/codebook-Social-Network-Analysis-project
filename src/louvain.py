from __future__ import annotations
from typing import Dict, Set, List
import networkx as nx

def detect_communities_louvain(G: nx.Graph) -> Dict[str, int]:
    """
    Louvain community detection.

    Returns: dict {node_id: community_id}
    Requires: python-louvain package (imported as 'community').
    """
    try:
        import community as community_louvain  # python-louvain
    except Exception as e:
        raise ImportError(
            "python-louvain not installed. Run: pip install python-louvain"
        ) from e

    if G.number_of_nodes() == 0:
        return {}

    partition = community_louvain.best_partition(G)  # node -> community_id
    return partition

def communities_summary(partition: Dict[str,int]) -> List[tuple[int,int]]:
    """
    Returns list of (community_id, size) sorted by size desc.
    """
    from collections import Counter
    c = Counter(partition.values())
    return sorted(c.items(), key=lambda x: x[1], reverse=True)
