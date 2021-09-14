from controllers.user_controller import UserController
from tkinter import *
from pathlib import Path

class LoginPage(Frame):
  OUTPUT_PATH = Path(__file__).parent
  ASSETS_PATH = OUTPUT_PATH / Path("../assets")

  def __init__(self, window: Tk, todoPage: Frame) -> None:
    self.username = Entry
    self.user_controller = UserController()
    self.todo_page = todoPage
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

  def relative_assets_path(self, path: str) -> Path:
    return self.ASSETS_PATH / Path(path)

  def create_canvas(self):
    self.canvas.place(x = 0, y = 0)

    self.canvas.create_rectangle(
      431.0,
      0.0,
      862.0,
      519.0,
      fill="#FCFCFC",
      outline=""
    )
  
  def create_buttons(self):
    init_image_btn = PhotoImage(file = self.relative_assets_path("init_btn.png"))
    label = Label(image = init_image_btn)
    label.image = init_image_btn
    init_btn = Button(
      self,
      image = init_image_btn,
      borderwidth = 0,
      highlightthickness = 0,
      command = self.change_page,
      relief = "flat"
    )
    init_btn.place(
      x=561.0,
      y=296.0,
      width=180.0,
      height=55.0
    )

  def create_texts(self):
    self.canvas.create_text(
      478.0,
      63.0,
      anchor = "nw",
      text = "Se mantenha organizado\ncom o ",
      fill = "#5000B7",
      font = ("Roboto Bold", 26 * -1)
    )

    self.canvas.create_text(
      550.0,
      63.0,
      anchor="nw",
      text="\n To-Do List",
      fill="#000B6D",
      font=("Roboto Bold", 26 * -1)
    )

    self.canvas.create_text(
      561.0,
      182.0,
      anchor="nw",
      text="Insira seu nome/apelido",
      fill="#5000B7",
      font=("Roboto", 16 * -1)
    )

  def create_inputs(self):
    username_image = PhotoImage(file = self.relative_assets_path("username.png"))
    label = Label(image = username_image)
    label.image = username_image
    usernameBackground = self.canvas.create_image(
      650.5,
      248.5,
      image = username_image
    )

    self.username = Entry(
      self,
      bd = 0,
      bg = "#E1E7F7",
      highlightthickness = 0
    )

    self.username.place(
      x = 490.0,
      y = 218.0,
      width = 321.0,
      height = 59.0
    )

    background = PhotoImage(file = self.relative_assets_path("background.png"))
    label = Label(image=background)
    label.image = background
    self.canvas.create_image(
      261.0,
      360.0,
      image = background
    )

  def change_page(self):
    nome = self.username.get()
    result = self.user_controller.create(nome)
    if result:
      self.todo_page.canvas.itemconfig(self.todo_page.username_canvas, text = self.user_controller.nome)
      self.forget()
      self.todo_page.pack(fill = 'both', expand = 1)