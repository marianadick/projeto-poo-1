#Interface gráfica desenvolvida com o auxílio do "Tkinter Designer", por Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# Tela principal

# Imports necessários 

from pathlib import Path
from tkinter import *
import database.main as database
import methods

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

database.createTables()

window = Tk()

window.geometry("862x519")
window.configure(bg = "#D8E0F7")
window.title("To-do List")


canvas = Canvas(
    window,
    bg = "#D8E0F7",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.1368683772161603e-13,
    7.105427357601002e-15,
    431.0,
    519.0,
    fill="#FCFCFC",
    outline="")

# Botões 
deleteButtonImage = PhotoImage(file = relative_to_assets("botão_deletar.png"))
deleteButton = Button(
    image = deleteButtonImage,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: methods.delete(database, tasks),
    relief = "flat"
).place(
    x = 297.0,
    y = 359.0,
    width = 100.0,
    height = 35.0
)

addButtonImg = PhotoImage(file = relative_to_assets("botão_adicionar.png"))
addButton = Button(
    image = addButtonImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: methods.add_item(tasks, database, inputTask.get()),
    relief = "flat"
).place(
    x = 35.0,
    y = 359.0,
    width = 100.0,
    height = 35.0
)

buttonViewAllImg = PhotoImage(file = relative_to_assets("botão_view.png"))
buttonViewAll = Button(
    image = buttonViewAllImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: methods.refresh(True, tasks, database.getAll()),
    relief = "flat"
).place(
    x = 373.0,
    y = 308.0,
    width = 24.0,
    height = 24.0
)

buttonSearchImg = PhotoImage(file = relative_to_assets("botão_lupa.png"))
buttonSearch = Button(
    image = buttonSearchImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: methods.search(database, inputTask.get(), tasks),
    relief = "flat"
).place(
    x = 335.0,
    y = 311.0,
    width = 23.0,
    height = 23.0
)

buttonEditImg = PhotoImage(
    file=relative_to_assets("botão_editar.png"))
buttonEdit = Button(
    image = buttonEditImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: methods.edit(database, tasks, inputTask.get()),
    relief = "flat"
).place(
    x = 166.0,
    y = 359.0,
    width = 100.0,
    height = 35.0
)

# Textos
canvas.create_text(
    41.0,
    126.0,
    anchor = "nw",
    text = "Seja bem-vindo(a),\n",
    fill = "#5000B7",
    font = ("Roboto Bold", 26 * -1)
)

canvas.create_text(
    41.0,
    156.0,
    anchor = "nw",
    text = "nome_do_usuário",
    fill = "#000B6D",
    font = ("Roboto Bold", 26 * -1)
)

canvas.create_text(
    41.0,
    223.0,
    anchor = "nw",
    text = "Adicione novas tarefas ou edite a tarefa\nselecionada utilizando as ferramentas abaixo.",
    fill = "#5000B7",
    font = ("Roboto", 16 * -1)
)

canvas.create_text(
    41.0,
    285.0,
    anchor = "nw",
    text = "Nome da tarefa",
    fill = "#5000B7",
    font = ("Roboto Thin", 16 * -1)
)

# Entradas de texto 
inputImage = PhotoImage(file = relative_to_assets("entrada_2.png"))
inputBackground = canvas.create_image(
    180.0,
    322.5,
    image=inputImage
)
inputTask = Entry(
    bd = 0,
    bg = "#D8E0F7",
    highlightthickness = 0
)
inputTask.place(
    x = 52.0,
    y = 305.0,
    width = 256.0,
    height = 33.0
)

# Imagens 
img01 = PhotoImage(file = relative_to_assets("ilustração_2.png"))
image_1 = canvas.create_image(
    678.0,
    295.0,
    image = img01
)

# Listbox e scrollbar
tasks = Listbox(borderwidth = 0, height = 14, width = 34)
tasks.place(x = 490, y = 121)

tasks_scroll = Scrollbar()
tasks_scroll.place(x = 701, y = 160)

tasks.configure(yscrollcommand = tasks_scroll.set)
tasks_scroll.configure(command = tasks.yview)

def onselect(evt):
  widget = evt.widget
  index = int(widget.curselection()[0])
  value = widget.get(index)
  inputTask.delete(0, END)
  inputTask.insert(0, value)

tasks.bind('<<ListboxSelect>>', onselect)

methods.refresh(True, tasks, database.getAll())

window.resizable(False, False)
window.mainloop()
