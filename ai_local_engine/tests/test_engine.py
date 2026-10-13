import sqlite3
import os
import pytest
from ai_local_engine.engine import SyncEngine

@pytest.fixture
def setup_db(tmp_path):
    db_file = tmp_path / "test.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, desc TEXT)")
    cursor.execute("INSERT INTO products VALUES (1, 'Laptop', 'High performance laptop')")
    cursor.execute("INSERT INTO products VALUES (2, 'Phone', 'Smart mobile phone')")
    conn.commit()
    conn.close()
    return str(db_file)

def test_sync_engine(setup_db, tmp_path):
    cache_file = str(tmp_path / "vector_cache.json")
    engine = SyncEngine(db_path=setup_db, license_key="PRO-12345", cache_path=cache_file)
    
    updated = engine.sync_table("products", ["name", "desc"])
    assert updated == 2

    updated_again = engine.sync_table("products", ["name", "desc"])
    assert updated_again == 0
