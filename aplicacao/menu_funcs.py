import tkinter as tk
from tkinter import PhotoImage
import sys
import os
from tkinter.filedialog import askdirectory

class MenuFuncs:
    def exibir_imagem(self):
        janela_imagem = tk.Toplevel()
        janela_imagem.title("Imagem")

        imagem = PhotoImage(file="caminho/para/sua/imagem.png")  # Substitua pelo caminho da sua imagem

        label_imagem = tk.Label(janela_imagem, image=imagem)
        label_imagem.pack()

        label_imagem.bind("<Button-1>", lambda e: janela_imagem.destroy())

    def opcao1(self, text_widget):
        mensagem = "Opção 1 selecionada"
        text_widget.insert(tk.END, mensagem + "\n")

    def opcao2(self, text_widget):
        mensagem = "Opção 2 selecionada"
        text_widget.insert(tk.END, mensagem + "\n")

    def sub_opcao1(self, text_widget):
        
        mensagem = "Sub-opção 1 selecionada"
        text_widget.insert(tk.END, mensagem + "\n")

    def sub_opcao2(self, text_widget):
        mensagem = "Sub-opção 2 selecionada"
        text_widget.insert(tk.END, mensagem + "\n")

    def sub_submenu1(self, text_widget):
        origem = askdirectory(title="Pasta Origem")
        print(origem)
        arquivos=os.listdir(origem)
        resultado = f" Os arquivos do diretório {origem} são:\n\n"
        for i in arquivos:  # Lista Diretorio
            resultado += f"{i} \n"
        # mensagem = "Sub-submenu 1 selecionado"
        text_widget.insert(tk.END, resultado + "\n")

    def sub_submenu2(self, text_widget):
        mensagem = "Arquivos Organizados com Sucesso!"
        caminho = askdirectory(title="Selecione um diretório")

        lista_arquivos = os.listdir(caminho)
        print(lista_arquivos) 
        locais={
            "imagens":[".jpg",".png",".jpeg",".tif",".tiff"],
            "planilhas":[".xls",".xlsx"],
            "documentos":[".doc",".docx",".txt"],
            "pdfs":[".pdf"],
            "csv":[".csv"],
        }
        for arquivo in lista_arquivos:
            nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
            for pasta in locais:
                if extensao in locais[pasta]:
                    if not os.path.exists(f"{caminho}/{pasta}"):
                        os.mkdir(f"{caminho}/{pasta}")
                    os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")
        text_widget.insert(tk.END, mensagem + "\n")

    def sub_submenu3(self, text_widget):
        mensagem = "Sub-submenu 3 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")

    def sub_submenu4(self, text_widget):
        mensagem = "Sub-submenu 4 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")

    def submenu_com_menu_interno_1(self, text_widget):
        mensagem = "Submenu com Menu Interno 1 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")

    def submenu_com_menu_interno_2(self, text_widget):
        mensagem = "Submenu com Menu Interno 2 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")

    def submenu_com_menu_interno_3(self, text_widget):
        mensagem = "Submenu com Menu Interno 3 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")

    def submenu_com_menu_interno_4(self, text_widget):
        mensagem = "Submenu com Menu Interno 4 selecionado"
        text_widget.insert(tk.END, mensagem + "\n")
