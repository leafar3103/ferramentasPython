import tkinter as tk

def opcao1():
    print("Opção 1 selecionada")

def opcao2():
    print("Opção 2 selecionada")

def sub_opcao1():
    print("Sub-opção 1 selecionada")

def sub_opcao2():
    print("Sub-opção 2 selecionada")

def sub_submenu1():
    print("Sub-submenu 1 selecionado")

def sub_submenu2():
    print("Sub-submenu 2 selecionado")

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Submenus")

# Criar o menu principal
menu_principal = tk.Menu(root)

# Adicionar opções ao menu principal
menu_principal.add_command(label="Opção 1", command=opcao1)
menu_principal.add_command(label="Opção 2", command=opcao2)

# Criar um submenu
submenu = tk.Menu(menu_principal, tearoff=0)
submenu.add_command(label="Sub-opção base", command=sub_opcao1)
submenu.add_command(label="Sub-opção 2", command=sub_opcao2)

# Criar um sub-submenu
sub_submenu = tk.Menu(submenu, tearoff=0)
sub_submenu.add_command(label="Sub-submenu 1", command=sub_submenu1)
sub_submenu.add_command(label="Sub-submenu 2", command=sub_submenu2)

# Adicionar o sub-submenu ao submenu
submenu.add_cascade(label="Sub-submenu", menu=sub_submenu)

# Adicionar o submenu ao menu principal
menu_principal.add_cascade(label="Submenu", menu=submenu)

# Configurar o menu principal na janela
root.config(menu=menu_principal)

# Iniciar o loop da aplicação
root.mainloop()
