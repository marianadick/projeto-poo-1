from controllers.TasksController import TasksController
from tkinter import *
from pathlib import Path

class TodoPage(Frame):
  OUTPUT_PATH = Path(__file__).parent
  ASSETS_PATH = OUTPUT_PATH / Path("../assets")

  def __init__(self, window: Tk) -> None:
    self.tasksController = TasksController()
    self.usernameCanvas = str
    self.inputTask = Entry
    super().__init__(window)
    self.canvas = Canvas(
      self,
      bg = "#D8E0F7",
      height = 519,
      width = 862,
      bd = 0,
      highlightthickness = 0,
      relief = "ridge"
    )
    self.createCanvas()
    self.createButtons()
    self.createTexts()
    self.createInputs()


    self.tasks = Listbox(self, borderwidth = 0, height = 14, width = 34)
    self.tasks.place(x = 490, y = 121)
    tasks_scroll = Scrollbar(self)
    tasks_scroll.place(x = 701, y = 200)
    self.tasks.configure(yscrollcommand = tasks_scroll.set)
    tasks_scroll.configure(command = self.tasks.yview)

    self.tasks.bind('<<ListboxSelect>>', self.onselect)
    self.tasks.bind('<Double-1>', self.check)

    self.tasksController.refresh(True, self.tasks)

  def relativeAssetsPath(self, path: str) -> Path:
    return self.ASSETS_PATH / Path(path)

  def createCanvas(self):
    self.canvas.place(x = 0, y = 0)

    self.canvas.create_rectangle(
      1.1368683772161603e-13,
      7.105427357601002e-15,
      862.0,
      519.0,
      fill="#FCFCFC",
      outline=""
    )
  
  def createButtons(self):
    deleteImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_deletar.png"))
    label = Label(image = deleteImageBtn)
    label.image = deleteImageBtn
    deleteBtn = Button(
      self,
      image = deleteImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasksController.delete(self.tasks),
      relief = "flat"
    )
    deleteBtn.place(
      x = 297.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

    addImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_adicionar.png"))
    label = Label(image = addImageBtn)
    label.image = addImageBtn
    addBtn = Button(
      self,
      image = addImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasksController.create(self.tasks, self.inputTask.get()),
      relief = "flat"
    )
    addBtn.place(
      x = 35.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

    viewAllImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_view.png"))
    label = Label(image = viewAllImageBtn)
    label.image = viewAllImageBtn
    viewAllBtn = Button(
      self,
      image = viewAllImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasksController.refresh(True, self.tasks),
      relief = "flat"
    )
    viewAllBtn.place(
      x = 373.0,
      y = 308.0,
      width = 24.0,
      height = 24.0
    )

    seacrhImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_lupa.png"))
    label = Label(image = seacrhImageBtn)
    label.image = seacrhImageBtn
    searchBtn = Button(
      self,
      image = seacrhImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasksController.find(self.tasks, self.inputTask.get()),
      relief = "flat"
    )
    searchBtn.place(
      x = 335.0,
      y = 311.0,
      width = 23.0,
      height = 23.0
    )

    editImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_editar.png"))
    label = Label(image = editImageBtn)
    label.image = editImageBtn
    editBtn = Button(
      self,
      image = editImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasksController.update(self.tasks, self.inputTask.get()),
      relief = "flat"
    )
    editBtn.place(
      x = 166.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

  def createTexts(self):
    self.canvas.create_text(
      41.0,
      126.0,
      anchor = "nw",
      text = "Seja bem-vindo(a),\n",
      fill = "#5000B7",
      font = ("Roboto Bold", 26 * -1)
    )

    self.usernameCanvas = self.canvas.create_text(
      41.0,
      156.0,
      anchor = "nw",
      text = "",
      fill = "#000B6D",
      font = ("Roboto Bold", 26 * -1)
    )

    self.canvas.create_text(
      41.0,
      223.0,
      anchor = "nw",
      text = "Adicione novas tarefas ou edite a tarefa\nselecionada utilizando as ferramentas abaixo.",
      fill = "#5000B7",
      font = ("Roboto", 16 * -1)
    )

    self.canvas.create_text(
      41.0,
      285.0,
      anchor = "nw",
      text = "Nome da tarefa",
      fill = "#5000B7",
      font = ("Roboto Thin", 16 * -1)
    )

    self.canvas.create_text(
      561.0,
      182.0,
      anchor="nw",
      text="Insira seu nome/apelido",
      fill="#5000B7",
      font=("Roboto", 16 * -1)
    )

  def createInputs(self):
    inputImage = PhotoImage(file = self.relativeAssetsPath("entrada_2.png"))
    label = Label(image = inputImage)
    label.image = inputImage
    inputBackground = self.canvas.create_image(
      180.0,
      322.5,
      image = inputImage
    )
    self.inputTask = Entry(
      self,
      bd = 0,
      bg = "#D8E0F7",
      highlightthickness = 0
    )
    self.inputTask.place(
      x = 52.0,
      y = 305.0,
      width = 256.0,
      height = 33.0
    )

    background2 = PhotoImage(file = self.relativeAssetsPath("ilustração_2.png"))
    label = Label(image=background2)
    label.image = background2
    self.canvas.create_image(
      678.0,
      295.0,
      image = background2
    )

  def onselect(self, evt):
    try:
      widget = evt.widget
      index = int(widget.curselection()[0])
      value = widget.get(index)
      self.inputTask.delete(0, END)
      self.inputTask.insert(0, value.replace("✓", ""))
    except:
      pass

  def check(self, evt):
    try:
      widget = evt.widget
      index = int(widget.curselection()[0])
      value = widget.get(index)
      find = value.find("✓")
      if find >= 0:
        self.tasksController.uncomplete(self.tasks, index)
      else:
        self.tasksController.complete(self.tasks, index)
    except:
      pass