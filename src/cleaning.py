from __future__ import annotations
from typing import Any, Dict, List

def normalize_users(raw: Any) -> List[Dict[str, Any]]:
    # Supports list[dict] or dict with 'users'
    if isinstance(raw, dict) and "users" in raw:
        users = raw["users"]
    else:
        users = raw

    if not isinstance(users, list):
        return []

    cleaned: List[Dict[str, Any]] = []
    seen=set()

    for u in users:
        if not isinstance(u, dict):
            continue
        uid = str(u.get("id") or u.get("user_id") or u.get("username") or "").strip()
        if not uid or uid in seen:
            continue
        seen.add(uid)

        friends = u.get("friends") or u.get("connections") or []
        pages = u.get("pages") or u.get("likes") or []

        if friends is None: friends=[]
        if pages is None: pages=[]

        cleaned.append({
            "id": uid,
            "name": u.get("name") or u.get("username") or uid,
            "friends": [str(x) for x in friends if str(x).strip()],
            "pages": [str(x) for x in pages if str(x).strip()],
        })

    return cleaned
