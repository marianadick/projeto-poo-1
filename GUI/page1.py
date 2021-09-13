import tkinter as tk
from pathlib import Path
import methods
from main import Page
import database.main as database

database.createTables()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
  print(ASSETS_PATH / Path(path))
  return ASSETS_PATH / Path(path)

class Page1(Page):
  def __init__(self, *args, **kwargs):
    Page.__init__(self, *args, **kwargs)
    
    canvas = tk.Canvas(
    self,
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
    deleteButtonImage = tk.PhotoImage(file = relative_to_assets("botão_deletar.png"))
    deleteButton = tk.Button(
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

    addButtonImg = tk.PhotoImage(file = relative_to_assets("botão_adicionar.png"))
    addButton = tk.Button(
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

    buttonViewAllImg = tk.PhotoImage(file = relative_to_assets("botão_view.png"))
    buttonViewAll = tk.Button(
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

    buttonSearchImg = tk.PhotoImage(file = relative_to_assets("botão_lupa.png"))
    buttonSearch = tk.Button(
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

    buttonEditImg = tk.PhotoImage(
        file=relative_to_assets("botão_editar.png"))
    buttonEdit = tk.Button(
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
    inputImage = tk.PhotoImage(file = relative_to_assets("entrada_2.png"))
    inputBackground = canvas.create_image(
        180.0,
        322.5,
        image=inputImage
    )
    inputTask = tk.Entry(
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
    img01 = tk.PhotoImage(file = relative_to_assets("ilustração_2.png"))
    image_1 = canvas.create_image(
        678.0,
        295.0,
        image = img01
    )

    # Listbox e scrollbar
    tasks = tk.Listbox(borderwidth = 0, height = 14, width = 34)
    tasks.place(x = 490, y = 121)

    tasks_scroll = tk.Scrollbar()
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
