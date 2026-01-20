from __future__ import annotations
from pathlib import Path
from typing import Any, List
from .utils import read_json

DEFAULT_FILES = ["data.json", "data2.json", "massive_data.json"]

def load_datasets(data_dir: Path) -> List[Any]:
    datasets = []
    for name in DEFAULT_FILES:
        p = data_dir / name
        if p.exists():
            datasets.append(read_json(p))
    return datasets
