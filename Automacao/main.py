# main.py
import tkinter as tk
from tkinter import PhotoImage
from funcoes import opcao1, opcao2, sub_opcao1, sub_opcao2, sub_submenu1, sub_submenu2, sub_submenu3, sub_submenu4
from funcoes import submenu_com_menu_interno_1, submenu_com_menu_interno_2, submenu_com_menu_interno_3, submenu_com_menu_interno_4

def exibir_imagem():
    # Criar uma nova janela
    janela_imagem = tk.Toplevel(root)
    janela_imagem.title("Imagem")

    # Carregar a imagem
    imagem = PhotoImage(file="caminho/para/sua/imagem.png")  # Substitua pelo caminho da sua imagem

    # Criar um rótulo para exibir a imagem
    label_imagem = tk.Label(janela_imagem, image=imagem)
    label_imagem.pack()

    # Fechar a janela ao clicar na imagem
    label_imagem.bind("<Button-1>", lambda e: janela_imagem.destroy())

def chamar_funcao(funcao):
    resultado_text.delete(1.0, tk.END)  # Limpa o conteúdo atual
    funcao(resultado_text)  # Chama a função e atualiza o resultado

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Submenus")

# Criar o menu principal
menu_principal = tk.Menu(root)

# Adicionar opções ao menu principal
opcoes = [
    ("Opção 1", opcao1),
    ("Opção 2", opcao2),
]

for opcao, funcao in opcoes:
    menu_principal.add_command(label=opcao, command=lambda f=funcao: chamar_funcao(f))

# Criar um submenu
submenu = tk.Menu(menu_principal, tearoff=0)

sub_opcoes = [
    ("Sub-opção 1", sub_opcao1),
    ("Sub-opção 2", sub_opcao2),
]

for sub_opcao, funcao in sub_opcoes:
    submenu.add_command(label=sub_opcao, command=lambda f=funcao: chamar_funcao(f))

# Criar um sub-submenu
sub_submenu = tk.Menu(submenu, tearoff=0)

sub_sub_opcoes = [
    ("Sub-submenu 1", sub_submenu1),
    ("Sub-submenu 2", sub_submenu2),
    ("Sub-submenu 3", sub_submenu3),
    ("Sub-submenu 4", sub_submenu4),
]

for sub_sub_opcao, funcao in sub_sub_opcoes:
    sub_submenu.add_command(label=sub_sub_opcao, command=lambda f=funcao: chamar_funcao(f))

submenu.add_cascade(label="Sub-submenu", menu=sub_submenu)

# Adicionar submenus com menus internos
submenus_com_menu_interno = [
    ("Menu Interno 1", submenu_com_menu_interno_1),
    ("Menu Interno 2", submenu_com_menu_interno_2),
    ("Menu Interno 3", submenu_com_menu_interno_3),
    ("Menu Interno 4", submenu_com_menu_interno_4),
]

for submenu_interno, funcao in submenus_com_menu_interno:
    submenu_com_menu_interno = tk.Menu(submenu, tearoff=0)
    
    submenu_com_menu_interno.add_command(label="Item 1", command=lambda f=funcao: chamar_funcao(f))
    submenu_com_menu_interno.add_command(label="Item 2", command=lambda f=funcao: chamar_funcao(f))
    submenu_com_menu_interno.add_command(label="Item 3", command=lambda f=funcao: chamar_funcao(f))

    submenu.add_cascade(label=submenu_interno, menu=submenu_com_menu_interno)

# Adicionar o submenu ao menu principal
menu_principal.add_cascade(label="Submenu", menu=submenu)

# Configurar o menu principal na janela
root.config(menu=menu_principal)

# Criar um widget Text para exibir resultados
resultado_text = tk.Text(root, height=10, width=40)
resultado_text.pack(pady=10)

# Criar um botão para exibir a imagem
botao_exibir_imagem = tk.Button(root, text="Exibir Imagem", command=exibir_imagem)
botao_exibir_imagem.pack(pady=10)

# Iniciar o loop da aplicação
root.mainloop()
