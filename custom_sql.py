import sqlite3
import os
import pathlib

# Directory Paths
BASE_DIR = pathlib.Path(__file__).parent


class db_requests:
    def __init__(self):
        if not os.path.isfile(BASE_DIR / "db.db"):
            self.conn = sqlite3.connect("db.db")
            self.c = self.conn.cursor()
            self.create_db()
        else:
            self.conn = sqlite3.connect("db.db")
            self.c = self.conn.cursor()

    def create_db(self):
        with open("script.sql", "r") as f:
            sql = f.read()
        self.c.executescript(sql)

    def list_items(self):
        self.c.execute("SELECT id,bez,vpreis,lagerbestand FROM produkt;")
        return self.c.fetchall()

    def list_one_item(self, item_id):
        self.c.execute(
            "SELECT id,bez,vpreis,lagerbestand FROM produkt WHERE id=?;", str(item_id)
        )
        return self.c.fetchall()

    def restock(self, item_id):
        self.c.execute(
            "SELECT id,bez,vpreis,lagerbestand FROM produkt WHERE lagerbestand <= 20;",
            str(item_id),
        )
        return self.c.fetchall()


if __name__ == "__main__":
    db = db_requests()
