import sqlite3
from typing import List, Dict, Any

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_records(self, table_name: str, text_columns: List[str]) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cols = ", ".join(text_columns)
        query = f"SELECT id, {cols} FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        records = []
        for row in rows:
            record_id = str(row[0])
            content = " | ".join([str(v) for v in row[1:] if v is not None])
            records.append({"id": record_id, "content": content})
        return records
