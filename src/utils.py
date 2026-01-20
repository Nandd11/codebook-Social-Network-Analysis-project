from __future__ import annotations
import json
from pathlib import Path
from typing import Any

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8', errors='ignore'))

def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
