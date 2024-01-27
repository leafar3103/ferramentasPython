import tkinter as tk
from tkinter import PhotoImage
from menu_funcs import MenuFuncs

class AplicacaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramentas SI")
        self.root.geometry("800x300")
        self.menu_funcs = MenuFuncs()

        self.criar_menu()
        self.criar_widgets()

    def chamar_funcao(self, funcao):
        self.resultado_text.delete(1.0, tk.END)  # Limpa o conteúdo atual
        funcao(self.resultado_text)  # Chama a função e atualiza o resultado

    def criar_menu(self):
        self.menu_principal = tk.Menu(self.root)

        opcoes = [
            ("Opção 1", self.menu_funcs.opcao1),
            ("Opção 2", self.menu_funcs.opcao2),
        ]

        for opcao, funcao in opcoes:
            self.menu_principal.add_command(label=opcao, command=lambda f=funcao: self.chamar_funcao(f))

        self.submenu = tk.Menu(self.menu_principal, tearoff=0)

        sub_opcoes = [
            ("Sub-opção 1", self.menu_funcs.sub_opcao1),
            ("Sub-opção 2", self.menu_funcs.sub_opcao2),
        ]

        for sub_opcao, funcao in sub_opcoes:
            self.submenu.add_command(label=sub_opcao, command=lambda f=funcao: self.chamar_funcao(f))

        sub_submenu = tk.Menu(self.submenu, tearoff=0)

        sub_sub_opcoes = [
            ("Sub-submenu 1", self.menu_funcs.sub_submenu1),
            ("Organiza", self.menu_funcs.sub_submenu2),
            ("Sub-submenu 3", self.menu_funcs.sub_submenu3),
            ("Sub-submenu 4", self.menu_funcs.sub_submenu4),
        ]

        for sub_sub_opcao, funcao in sub_sub_opcoes:
            sub_submenu.add_command(label=sub_sub_opcao, command=lambda f=funcao: self.chamar_funcao(f))

        self.submenu.add_cascade(label="Sub-submenu", menu=sub_submenu)

        submenus_com_menu_interno = [
            ("Menu Interno 1", self.menu_funcs.submenu_com_menu_interno_1),
            ("Menu Interno 2", self.menu_funcs.submenu_com_menu_interno_2),
            ("Menu Interno 3", self.menu_funcs.submenu_com_menu_interno_3),
            ("Menu Interno 4", self.menu_funcs.submenu_com_menu_interno_4),
        ]

        for submenu_interno, funcao in submenus_com_menu_interno:
            submenu_com_menu_interno = tk.Menu(self.submenu, tearoff=0)

            submenu_com_menu_interno.add_command(label="Item 1", command=lambda f=funcao: self.chamar_funcao(f))
            submenu_com_menu_interno.add_command(label="Item 2", command=lambda f=funcao: self.chamar_funcao(f))
            submenu_com_menu_interno.add_command(label="Item 3", command=lambda f=funcao: self.chamar_funcao(f))

            self.submenu.add_cascade(label=submenu_interno, menu=submenu_com_menu_interno)

        self.menu_principal.add_cascade(label="Submenu", menu=self.submenu)
        self.root.config(menu=self.menu_principal)

    def criar_widgets(self):
        self.resultado_text = tk.Text(self.root, height=10, width=40)
        self.resultado_text.pack(pady=10)

        botao_exibir_imagem = tk.Button(self.root, text="Exibir Imagem", command=self.menu_funcs.exibir_imagem)
        botao_exibir_imagem.pack(pady=10)
