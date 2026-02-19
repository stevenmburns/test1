import sqlite3


class KeyValueStore:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS store (key TEXT PRIMARY KEY, value TEXT)"
        )
        self.conn.commit()

    def set(self, key: str, value: str) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO store (key, value) VALUES (?, ?)", (key, value)
        )
        self.conn.commit()

    def get(self, key: str) -> str | None:
        row = self.conn.execute(
            "SELECT value FROM store WHERE key = ?", (key,)
        ).fetchone()
        return row[0] if row else None

    def delete(self, key: str) -> None:
        self.conn.execute("DELETE FROM store WHERE key = ?", (key,))
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
