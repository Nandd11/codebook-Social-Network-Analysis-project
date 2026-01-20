from __future__ import annotations
import networkx as nx
from typing import Dict, List, Tuple

def compute_metrics(G: nx.Graph) -> Dict[str, Dict[str, float]]:
    degree = nx.degree_centrality(G) if G.number_of_nodes() else {}
    betweenness = nx.betweenness_centrality(G, normalized=True) if G.number_of_nodes() else {}
    pagerank = nx.pagerank(G) if G.number_of_nodes() else {}
    return {
        "degree_centrality": degree,
        "betweenness_centrality": betweenness,
        "pagerank": pagerank,
    }

def top_n(metric: Dict[str, float], n: int = 5) -> List[Tuple[str, float]]:
    return sorted(metric.items(), key=lambda x: x[1], reverse=True)[:n]
