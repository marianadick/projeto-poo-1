from database.main import Database

class UserController():
  def __init__(self) -> None:
    self.id = int
    self.nome = str
    self.dao = Database("to-do.db")

  def create(self, nome) -> bool:
    nome = nome.strip()
    if nome != "":
      self.dao.cursor.execute("INSERT INTO users (name) VALUES (?)", (nome, ))
      self.dao.database.commit()
      self.nome = nome
      return True
    else:
      return False