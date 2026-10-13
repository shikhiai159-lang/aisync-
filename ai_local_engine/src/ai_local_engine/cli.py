import argparse
import sys
from ai_local_engine.engine import SyncEngine

def main():
    parser = argparse.ArgumentParser(description="Local-First SQLite & Hybrid Vector Database Sync Engine")
    parser.add_argument("--db", required=True, help="Path to SQLite database file")
    parser.add_argument("--table", required=True, help="Table name to sync")
    parser.add_argument("--cols", required=True, nargs="+", help="Text columns to process for vector embedding")
    parser.add_argument("--key", default="", help="Pro License Key")
    parser.add_argument("--cache", default="vector_cache.json", help="Path to vector cache file")

    args = parser.parse_args()

    print(f"🚀 Starting Sync Engine for table: {args.table}...")
    try:
        engine = SyncEngine(db_path=args.db, license_key=args.key, cache_path=args.cache)
        updated_count = engine.sync_table(args.table, args.cols)
        print(f"✅ Sync completed successfully! Total updated records: {updated_count}")
    except Exception as e:
        print(f"❌ Error during sync: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
