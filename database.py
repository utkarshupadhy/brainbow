import json
import sqlite3
from datetime import datetime

DB_PATH = "brainbow.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            '''CREATE TABLE IF NOT EXISTS screenings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                answers TEXT NOT NULL,
                score INTEGER NOT NULL,
                percentage REAL NOT NULL,
                category TEXT NOT NULL
            )'''
        )
        conn.commit()

def save_screening(answers, result):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO screenings (created_at, answers, score, percentage, category) VALUES (?, ?, ?, ?, ?)",
            (
                datetime.now().isoformat(timespec="seconds"),
                json.dumps(answers),
                result["score"],
                result["percentage"],
                result["category"],
            ),
        )
        conn.commit()

def get_recent_screenings(limit=10):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, created_at, score, percentage, category FROM screenings ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]
