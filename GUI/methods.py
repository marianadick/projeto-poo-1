import database.main as database
aux = []

def refresh(first, lista, items):
  if first:
    lista.delete(0, lista.size())
    for item in items:
      lista.insert(item[0], item[1])
      aux.insert(lista.size() - 1, item[0])
  else: 
    lista.insert(items[0], items[1])
    aux.insert(lista.size() - 1, items[0])

def add_item(lista, database, nome):
  id = database.store(nome)
  task = [id, nome]
  refresh(False, lista, task)

def search(database, nome, lista):
  items = database.findByName(nome)
  lista.delete(0, lista.size())
  aux = []
  for task in items:
    lista.insert(task[0], task[1])
    aux.insert(lista.size() - 1, task[0])

def edit(database, lista, nome):
  id = aux[lista.curselection()[0]]
  database.update(id, nome)
  lista.delete(0, lista.size())
  refresh(True, lista, database.getAll())

def delete(database, lista):
  id = aux[lista.curselection()[0]]
  database.delete(id)
  lista.delete(0, lista.size())
  refresh(True, lista, database.getAll())

def add_user(name):
  database.storeUser(name)