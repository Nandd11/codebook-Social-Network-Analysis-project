from __future__ import annotations
import networkx as nx
from typing import Dict, Any, List

def build_graph(users: List[Dict[str, Any]]) -> nx.Graph:
    G = nx.Graph()
    for u in users:
        uid = u["id"]
        G.add_node(uid, name=u.get("name",""), pages=u.get("pages",[]))
    for u in users:
        uid = u["id"]
        for fid in u.get("friends", []):
            if fid == uid:
                continue
            G.add_edge(uid, fid)
    return G
