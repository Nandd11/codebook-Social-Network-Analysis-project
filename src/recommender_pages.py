from __future__ import annotations
from typing import Dict, Any, List, Tuple
from collections import Counter

def pages_you_might_like(users: List[Dict[str, Any]], target_id: str, top_n: int = 5) -> List[Tuple[str,int]]:
    user_map = {u["id"]: u for u in users}
    if target_id not in user_map:
        return []

    liked = set(user_map[target_id].get("pages", []))
    scores = Counter()

    for u in users:
        if u["id"] == target_id:
            continue
        pages = set(u.get("pages", []))
        overlap = len(pages & liked)
        if overlap > 0:
            for p in pages - liked:
                scores[p] += overlap

    return scores.most_common(top_n)
