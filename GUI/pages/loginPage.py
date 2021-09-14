from controllers.UserController import UserController
from tkinter import *
from pathlib import Path

class LoginPage(Frame):
  OUTPUT_PATH = Path(__file__).parent
  ASSETS_PATH = OUTPUT_PATH / Path("../assets")

  def __init__(self, window: Tk, todoPage: Frame) -> None:
    self.username = Entry
    self.userController = UserController()
    self.todoPage = todoPage
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

  def relativeAssetsPath(self, path: str) -> Path:
    return self.ASSETS_PATH / Path(path)

  def createCanvas(self):
    self.canvas.place(x = 0, y = 0)

    self.canvas.create_rectangle(
      431.0,
      0.0,
      862.0,
      519.0,
      fill="#FCFCFC",
      outline=""
    )
  
  def createButtons(self):
    initImageBtn = PhotoImage(file = self.relativeAssetsPath("botão_iniciar.png"))
    label = Label(image = initImageBtn)
    label.image = initImageBtn
    initBtn = Button(
      self,
      image = initImageBtn,
      borderwidth = 0,
      highlightthickness = 0,
      command = self.change_page,
      relief = "flat"
    )
    initBtn.place(
      x=561.0,
      y=296.0,
      width=180.0,
      height=55.0
    )

  def createTexts(self):
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

  def createInputs(self):
    usernameImage = PhotoImage(file = self.relativeAssetsPath("entrada_1.png"))
    label = Label(image = usernameImage)
    label.image = usernameImage
    usernameBackground = self.canvas.create_image(
      650.5,
      248.5,
      image = usernameImage
    )

    self.username = Entry(
      self,
      bd = 0,
      bg = "#D8E0F7",
      highlightthickness = 0
    )

    self.username.place(
      x = 490.0,
      y = 218.0,
      width = 321.0,
      height = 59.0
    )

    background = PhotoImage(file = self.relativeAssetsPath("ilustração_1.png"))
    label = Label(image=background)
    label.image = background
    self.canvas.create_image(
      261.0,
      360.0,
      image = background
    )

  def change_page(self):
    nome = self.username.get()
    result = self.userController.create(nome)
    if result:
      self.canvas.itemconfig(self.todoPage.usernameCanvas, text = self.userController.nome)
      self.forget()
      self.todoPage.pack(fill='both', expand=1)