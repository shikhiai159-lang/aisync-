from typing import List
from ai_local_engine.database import DatabaseManager
from ai_local_engine.vector_store import VectorStore
from ai_local_engine.licensing import Licensing

class SyncEngine:
    def __init__(self, db_path: str, license_key: str = "", cache_path: str = "vector_cache.json"):
        self.db = DatabaseManager(db_path)
        self.vector_store = VectorStore(cache_path)
        self.licensing = Licensing()
        self.is_pro = self.licensing.verify(license_key)

    def sync_table(self, table_name: str, text_columns: List[str]) -> int:
        records = self.db.get_records(table_name, text_columns)
        
        if not self.is_pro and len(records) > 100:
            records = records[:100]

        updated_count = 0
        for rec in records:
            rec_id = rec["id"]
            content = rec["content"]
            text_hash = self.vector_store.generate_hash(content)

            if rec_id not in self.vector_store.cache or self.vector_store.cache[rec_id].get("hash") != text_hash:
                self.vector_store.cache[rec_id] = {
                    "id": rec_id,
                    "table": table_name,
                    "content": content,
                    "hash": text_hash,
                    "synced": True
                }
                updated_count += 1

        self.vector_store.save_cache()
        return updated_count
