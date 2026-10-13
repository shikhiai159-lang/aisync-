import json
import os
import hashlib
from typing import Dict, Any

class VectorStore:
    def __init__(self, cache_path: str = "vector_cache.json"):
        self.cache_path = cache_path
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict[str, Any]:
        if os.path.exists(self.cache_path):
            with open(self.cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_cache(self):
        with open(self.cache_path, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)

    def generate_hash(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()
