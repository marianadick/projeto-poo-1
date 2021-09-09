#Interface gráfica desenvolvida com o auxílio do "Tkinter Designer", por Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# Tela principal

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
    1.1368683772161603e-13,
    7.105427357601002e-15,
    431.0,
    519.0,
    fill="#FCFCFC",
    outline="")

# Botões 

botão_deletar_imagem = PhotoImage(
    file=relative_to_assets("botão_deletar.png"))
botão_deletar = Button(
    image=botão_deletar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão del clicado"),
    relief="flat"
)
botão_deletar.place(
    x=297.0,
    y=359.0,
    width=100.0,
    height=35.0
)

botão_adicionar_imagem = PhotoImage(
    file=relative_to_assets("botão_adicionar.png"))
botão_adicionar = Button(
    image=botão_adicionar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão add clicado"),
    relief="flat"
)
botão_adicionar.place(
    x=35.0,
    y=359.0,
    width=100.0,
    height=35.0
)

botão_visualizar_tudo_imagem = PhotoImage(
    file=relative_to_assets("botão_view.png"))
botão_visualizar_tudo = Button(
    image=botão_visualizar_tudo_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão view all clicado"),
    relief="flat"
)
botão_visualizar_tudo.place(
    x=373.0,
    y=308.0,
    width=24.0,
    height=24.0
)

botão_pesquisar_imagem = PhotoImage(
    file=relative_to_assets("botão_lupa.png"))
botão_pesquisar = Button(
    image=botão_pesquisar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão search clicado"),
    relief="flat"
)
botão_pesquisar.place(
    x=335.0,
    y=311.0,
    width=23.0,
    height=23.0
)

botão_editar_imagem = PhotoImage(
    file=relative_to_assets("botão_editar.png"))
botão_editar = Button(
    image=botão_editar_imagem,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("botão editar clicado"),
    relief="flat"
)
botão_editar.place(
    x=166.0,
    y=359.0,
    width=100.0,
    height=35.0
)

# Textos

canvas.create_text(
    41.0,
    126.0,
    anchor="nw",
    text="Seja bem-vindo(a),\n",
    fill="#5000B7",
    font=("Roboto Bold", 26 * -1)
)

canvas.create_text(
    41.0,
    156.0,
    anchor="nw",
    text="nome_do_usuário",
    fill="#000B6D",
    font=("Roboto Bold", 26 * -1)
)

canvas.create_text(
    41.0,
    223.0,
    anchor="nw",
    text="Adicione novas tarefas ou edite a tarefa\nselecionada utilizando as ferramentas abaixo.",
    fill="#5000B7",
    font=("Roboto", 16 * -1)
)

canvas.create_text(
    41.0,
    285.0,
    anchor="nw",
    text="Nome da tarefa",
    fill="#5000B7",
    font=("Roboto Thin", 16 * -1)
)

# Entradas de texto 

nome_da_tarefa_image = PhotoImage(
    file=relative_to_assets("entrada_2.png"))
nome_da_tarefa_bg = canvas.create_image(
    180.0,
    322.5,
    image=nome_da_tarefa_image
)
nome_da_tarefa = Entry(
    bd=0,
    bg="#D8E0F7",
    highlightthickness=0
)
nome_da_tarefa.place(
    x=52.0,
    y=305.0,
    width=256.0,
    height=33.0
)

# Imagens 

ilustração = PhotoImage(
    file=relative_to_assets("ilustração_2.png"))
image_1 = canvas.create_image(
    678.0,
    295.0,
    image=ilustração
)

# Listbox e scrollbar

lista = Listbox(borderwidth = 0, height = 14, width = 34)
lista.place(x = 490, y = 121)

lista_scroll= Scrollbar()
lista_scroll.place(x = 701, y = 160)

lista.configure(yscrollcommand=lista_scroll.set)
lista_scroll.configure(command=lista.yview)

window.resizable(False, False)
window.mainloop()
