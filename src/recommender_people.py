from __future__ import annotations
from typing import Dict, Any, List, Tuple
from collections import Counter

def people_you_may_know(users: List[Dict[str, Any]], target_id: str, top_n: int = 5) -> List[Tuple[str,int]]:
    user_map = {u["id"]: u for u in users}
    if target_id not in user_map:
        return []
    target_friends = set(user_map[target_id].get("friends", []))
    scores = Counter()

    for fid in target_friends:
        f = user_map.get(fid)
        if not f:
            continue
        for fof in f.get("friends", []):
            if fof == target_id or fof in target_friends:
                continue
            scores[fof] += 1

    return scores.most_common(top_n)
