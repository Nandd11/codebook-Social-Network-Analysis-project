from __future__ import annotations
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from typing import List, Set

def detect_communities(G: nx.Graph) -> List[Set[str]]:
    if G.number_of_nodes() == 0:
        return []
    # Greedy modularity (built-in NetworkX)
    comms = list(greedy_modularity_communities(G))
    return comms
