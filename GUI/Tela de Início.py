
#Interface gráfica desenvolvida com o auxílio do "Tkinter Designer", por Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# Tela de Início

# Imports necessários 

from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    image=botão_iniciar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão iniciar clicado"),
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

window.resizable(False, False)
window.mainloop()
