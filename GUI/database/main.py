import sqlite3
from sqlite3.dbapi2 import connect

class Database():
  def __init__(self, name) -> None:
    self.database = sqlite3.connect('GUI/database/' + name)
    self.cursor = self.database.cursor()

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        description TEXT NULL DEFAULT NULL,
        completed INTEGER DEFAULT 0
      )
    """)

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL
      )
    """)