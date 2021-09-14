from database.main import Database
from tkinter import Listbox

class TasksController():
	def __init__(self):
		self.ids = list()
		self.nome = str
		self.id = str
		self.dao = Database("to-do.db")

	def refresh(self, first: bool, lista: Listbox) -> None:
		tasks = self.get_all()
		if first:
			lista.delete(0, lista.size())
			for item in tasks:
				if item[3] == 1:
					lista.insert(item[0], self.strike(True, item[1]))
				else:
					lista.insert(item[0], item[1])
				self.ids.insert(lista.size() - 1, item[0])
		else: 
			lista.insert(self.id, self.nome)
			self.ids.insert(lista.size() - 1, self.id)
	
	def strike(self, complete: bool, text: str) -> str:
		if not complete:
			return text.replace(' ✓', '')
		else:
			return text + ' ✓'

	def create(self, lista: Listbox, nome: str) -> None:
		nome = nome.strip()
		if nome != "":
			self.dao.cursor.execute("INSERT INTO list (name) VALUES (?)", (nome, ))
			self.dao.database.commit()
			self.id = self.dao.cursor.lastrowid
			self.nome = nome
			self.refresh(False, lista)

	def complete(self, lista: Listbox, index: int) -> None:
		id = self.ids[index]
		self.dao.cursor.execute("UPDATE list SET completed = 1 WHERE id = ?", (id, ))
		self.dao.database.commit()
		self.refresh(True, lista)

	def uncomplete(self, lista: Listbox, index: int) -> None:
		id = self.ids[index]
		self.dao.cursor.execute("UPDATE list SET completed = 0 WHERE id = ?", (id, ))
		self.dao.database.commit()
		self.refresh(True, lista)

	def delete(self, lista: Listbox) -> None:
		id = self.ids[lista.curselection()[0]]
		self.dao.cursor.execute("DELETE FROM list WHERE id = ?", (id, ))
		self.dao.database.commit()
		lista.delete(0, lista.size())
		self.refresh(True, lista)

	def update(self, lista: Listbox, nome: str) -> None:
		id = self.ids[lista.curselection()[0]]
		self.dao.cursor.execute("UPDATE list SET name = ? WHERE id = ?", (nome, id))
		self.dao.database.commit()
		lista.delete(0, lista.size())
		self.refresh(True, lista)

	def find(self, lista: Listbox, nome: str) -> None:
		value = "%{}%".format(nome)
		items = self.dao.database.execute("SELECT * FROM list WHERE name LIKE ?", (value, ))
		lista.delete(0, lista.size())
		self.ids = []
		for task in items:
			lista.insert(task[0], task[1])
			self.ids.insert(lista.size() - 1, task[0])

	def get_all(self) -> list:
		result = self.dao.database.execute("SELECT * FROM list")
		return result