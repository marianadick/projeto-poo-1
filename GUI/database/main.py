import sqlite3
from sqlite3.dbapi2 import connect

# O método connect irá se conectar ao banco, ou caso
# ele não exista, irá criar.
database = sqlite3.connect('GUI/database/todo.db')

def createTable():
  database.execute("""
    CREATE TABLE IF NOT EXISTS list (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name VARCHAR(50) NOT NULL,
      description TEXT NULL DEFAULT NULL,
      completed INTEGER DEFAULT 0
    )
    """)

def store(name, desc):
  # Criar uma tarefa
  database.execute("INSERT INTO list (name, description) VALUES (?, ?)", (name, desc))
  database.commit()

def findByName(name):
  # Buscar uma tarefa pelo nome
  result = database.execute("SELECT * FROM list WHERE name LIKE ?", (name, ))
  return result.fetchall()

def findByPk(id):
  # Buscar uma tarefa pela primary key
  result = database.execute("SELECT * FROM list WHERE id = ?", (id, ))
  return result.fetchone()

def getAll():
  # Buscar todas as tarefas
  result = database.execute("SELECT * FROM list")
  return result.fetchall()

def delete(id):
  # Excluir uma tarefa
  database.execute("DELETE FROM list WHERE id = ?", (id, ))
  database.commit()

def finish(id):
  # Marcar uma tarefa como concluída
  database.execute("UPDATE list SET completed = 1 WHERE id = ?", (id, ))
  database.commit()

def back(id):
  # Desmarcar uma tarefa como concluída
  database.execute("UPDATE list SET completed = 0 WHERE id = ?", (id, ))
  database.commit()

def update(id, name, desc):
  # Atualiza uma tarefa
  database.execute("UPDATE list SET name = ?, description = ? WHERE id = ?", (name, desc, id))
  database.commit()
