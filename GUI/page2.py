from page1 import Page1
# import page1
import tkinter as tk
from pathlib import Path
import methods
from main import Page

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
  print(ASSETS_PATH / Path(path))
  return ASSETS_PATH / Path(path)

class Page2(Page):
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
      431.0,
      0.0,
      862.0,
      519.0,
      fill="#FCFCFC",
      outline="")

    # Botões
    buttonInitImg = tk.PhotoImage(file=relative_to_assets("botão_iniciar.png"))
    label = tk.Label(image=buttonInitImg)
    label.image = buttonInitImg

    botão_iniciar = tk.Button(
      image=buttonInitImg,
      borderwidth=0,
      highlightthickness=0,
      command= Page1.tkraise(),
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
    usernameImg = tk.PhotoImage(file=relative_to_assets("entrada_1.png"))
    label = tk.Label(image=usernameImg)
    label.image = usernameImg
    entry_bg_1 = canvas.create_image(
      650.5,
      248.5,
      image=usernameImg
    )
    nome_do_usuário = tk.Entry(
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

    img01 = tk.PhotoImage(file=relative_to_assets("ilustração_1.png"))
    label = tk.Label(image=img01)
    label.image = img01
    image_1 = canvas.create_image(
      261.0,
      360.0,
      image=img01
    )