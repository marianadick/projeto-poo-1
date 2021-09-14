from controllers.tasks_controller import TasksController
from tkinter import *
from pathlib import Path

class TodoPage(Frame):
  OUTPUT_PATH = Path(__file__).parent
  ASSETS_PATH = OUTPUT_PATH / Path("../assets")

  def __init__(self, window: Tk) -> None:
    self.tasks_controller = TasksController()
    self.username_canvas = str
    self.input_task = Entry
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
    self.create_canvas()
    self.create_buttons()
    self.create_texts()
    self.create_inputs()


    self.tasks = Listbox(self, borderwidth = 0, height = 14, width = 34)
    self.tasks.place(x = 490, y = 121)
    tasks_scroll = Scrollbar(self)
    tasks_scroll.place(x = 701, y = 200)
    self.tasks.configure(yscrollcommand = tasks_scroll.set)
    tasks_scroll.configure(command = self.tasks.yview)

    self.tasks.bind('<<ListboxSelect>>', self.onselect)
    self.tasks.bind('<Double-1>', self.check)

    self.tasks_controller.refresh(True, self.tasks)

  def relative_assets_path(self, path: str) -> Path:
    return self.ASSETS_PATH / Path(path)

  def create_canvas(self):
    self.canvas.place(x = 0, y = 0)

    self.canvas.create_rectangle(
      1.1368683772161603e-13,
      7.105427357601002e-15,
      431.0,
      519.0,
      fill="#FCFCFC",
      outline=""
    )
  
  def create_buttons(self):
    delete_image_btn = PhotoImage(file = self.relative_assets_path("delete_btn.png"))
    label = Label(image = delete_image_btn)
    label.image = delete_image_btn
    delete_btn = Button(
      self,
      image = delete_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasks_controller.delete(self.tasks),
      relief = "flat"
    )
    delete_btn.place(
      x = 297.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

    add_image_btn = PhotoImage(file = self.relative_assets_path("add_btn.png"))
    label = Label(image = add_image_btn)
    label.image = add_image_btn
    add_btn = Button(
      self,
      image = add_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasks_controller.create(self.tasks, self.input_task.get()),
      relief = "flat"
    )
    add_btn.place(
      x = 35.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

    view_all_image_btn = PhotoImage(file = self.relative_assets_path("view_all_btn.png"))
    label = Label(image = view_all_image_btn)
    label.image = view_all_image_btn
    view_all_btn = Button(
      self,
      image = view_all_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasks_controller.refresh(True, self.tasks),
      relief = "flat"
    )
    view_all_btn.place(
      x = 373.0,
      y = 308.0,
      width = 24.0,
      height = 24.0
    )

    search_image_btn = PhotoImage(file = self.relative_assets_path("search_btn.png"))
    label = Label(image = search_image_btn)
    label.image = search_image_btn
    search_btn = Button(
      self,
      image = search_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasks_controller.find(self.tasks, self.input_task.get()),
      relief = "flat"
    )
    search_btn.place(
      x = 335.0,
      y = 311.0,
      width = 23.0,
      height = 23.0
    )

    edit_image_btn = PhotoImage(file = self.relative_assets_path("edit_btn.png"))
    label = Label(image = edit_image_btn)
    label.image = edit_image_btn
    edit_btn = Button(
      self,
      image = edit_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = lambda: self.tasks_controller.update(self.tasks, self.input_task.get()),
      relief = "flat"
    )
    edit_btn.place(
      x = 166.0,
      y = 359.0,
      width = 100.0,
      height = 35.0
    )

  def create_texts(self):
    self.canvas.create_text(
      41.0,
      126.0,
      anchor = "nw",
      text = "Seja bem-vindo(a),\n",
      fill = "#5000B7",
      font = ("Roboto Bold", 26 * -1)
    )

    self.username_canvas = self.canvas.create_text(
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

  def create_inputs(self):
    input_image = PhotoImage(file = self.relative_assets_path("input.png"))
    label = Label(image = input_image)
    label.image = input_image
    input_background = self.canvas.create_image(
      180.0,
      322.5,
      image = input_image
    )
    self.input_task = Entry(
      self,
      bd = 0,
      bg = "#E1E7F7",
      highlightthickness = 0
    )
    self.input_task.place(
      x = 52.0,
      y = 305.0,
      width = 256.0,
      height = 33.0
    )

    background2 = PhotoImage(file = self.relative_assets_path("background_2.png"))
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
      self.input_task.delete(0, END)
      self.input_task.insert(0, value.replace("✓", ""))
    except:
      pass

  def check(self, evt):
    try:
      widget = evt.widget
      index = int(widget.curselection()[0])
      value = widget.get(index)
      find = value.find("✓")
      if find >= 0:
        self.tasks_controller.uncomplete(self.tasks, index)
      else:
        self.tasks_controller.complete(self.tasks, index)
    except:
      pass