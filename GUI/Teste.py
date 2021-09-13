from pathlib import Path
from tkinter import *
import database.main as database
import methods  


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def change_page():
    page1.forget()
    page2.pack(fill='both', expand=1)
    methods.add_user(nome_do_usuário.get())


window = Tk()

window.geometry("862x519")
window.configure(bg = "#D8E0F7")
window.title("To-do List")

page1 = Frame(window)
page2 = Frame(window)

# Tela de Início

canvas = Canvas(
    page1,
    bg = "#D8E0F7",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

# Botões

botão_iniciar_imagem = PhotoImage(
        file=relative_to_assets("botão_iniciar.png"))
botão_iniciar = Button(
    page1,
    image=botão_iniciar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=change_page,
    relief="flat"
)
botão_iniciar.place(
    x=561.0,
    y=296.0,
    width=180.0,
    height=55.0
)

# Textos

canvas.create_text(
    478.0,
    63.0,
    anchor="nw",
    text="Se mantenha organizado\ncom o ",
    fill="#5000B7",
    font=("Roboto Bold", 26 * -1)
)

canvas.create_text(
    550.0,
    63.0,
    anchor="nw",
    text="\n To-Do List",
    fill="#000B6D",
    font=("Roboto Bold", 26 * -1)
)

canvas.create_text(
    561.0,
    182.0,
    anchor="nw",
    text="Insira seu nome/apelido",
    fill="#5000B7",
    font=("Roboto", 16 * -1)
)

# Entradas de texto

nome_do_usuário_imagem = PhotoImage(
    file=relative_to_assets("entrada_1.png"))
entry_bg_1 = canvas.create_image(
    650.5,
    248.5,
    image=nome_do_usuário_imagem
)
nome_do_usuário = Entry(
    page1,
    bd=0,
    bg="#D8E0F7",
    highlightthickness=0
)
nome_do_usuário.place(
    x=490.0,
    y=218.0,
    width=321.0,
    height=59.0
)

# Imagens

ilustração = PhotoImage(
    file=relative_to_assets("ilustração_1.png"))
image_1 = canvas.create_image(
    261.0,
    360.0,
    image=ilustração
)

canvas = Canvas(
    page2,
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
    page2,
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
    page2,
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
    page2,
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
    page2,
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
    page2,
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

#Tela principal

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
    page2,
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
tasks = Listbox(page2, borderwidth = 0, height = 14, width = 34)
tasks.place(x = 490, y = 121)

tasks_scroll = Scrollbar(page2)
tasks_scroll.place(x = 701, y = 200)

tasks.configure(yscrollcommand = tasks_scroll.set)
tasks_scroll.configure(command = tasks.yview)

def onselect(evt):
	try:
		widget = evt.widget
		index = int(widget.curselection()[0])
		value = widget.get(index)
		inputTask.delete(0, END)
		inputTask.insert(0, value.replace("✓", ""))
	except:
		pass

def check(evt):
	try:
		widget = evt.widget
		index = int(widget.curselection()[0])
		value = widget.get(index)
		find = value.find("✓")
		if find >= 0:
			methods.back(tasks, index)
		else:
			methods.finish(tasks, index)
	except:
		pass
	

tasks.bind('<<ListboxSelect>>', onselect)
tasks.bind('<Double-1>', check)

methods.refresh(True, tasks, database.getAll())

page1.pack(fill='both', expand=1)

window.resizable(False, False)
window.mainloop()