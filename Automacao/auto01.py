import sys
import os
import platform
import subprocess
from time import sleep
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
# Testando comandos no sistema
# os.environ
os.getcwd()

os.listdir()

os.mkdir("teste")

sleep(5)

os.rmdir("teste")

# Criando interfaces com o tkinter

def funcao1():
    origem = askdirectory(title="Pasta Origem")
    print(origem)
    arquivos=os.listdir(origem)
    resultado = f" Os arquivos do diretório {origem} são:\n\n"
    for i in arquivos:  # Lista Diretorio
        resultado += f"{i} \n"  # Exemplo de cálculo simples
    resultado_label.config(text=resultado)

def funcao2():
    numero = 16  # Exemplo de número para calcular a raiz quadrada
    # resultado = f"A raiz quadrada de {numero} é {math.sqrt(numero):.2f}"
    # sistemOp= os.system("systeminfo" + "|" + "systeminfo | findstr  'Microsoft' ")
    sistemOp = platform.system()
    print(sistemOp)
    # resultado = sistemOp
    sleep(5)
    # resultado=numero*2
    resultado_label.config(text=sistemOp)
def funcao3():
    
    resultado=print("Ping Swep")
    resultado_label.config(text=resultado)
def mostrar_sobre():
    messagebox.showinfo("Sobre", "Vianna Security")


janela = tk.Tk()
janela.title("Testando o tk")
janela.geometry("800x300")

# Criar uma barra de menus
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)
# Criar um menu "Arquivo" com duas opções
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
scanning = tk.Menu(menu_arquivo, tearoff=1)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
# menu_arquivo.add_cascade(label="Scan", menu_arquivo=scanning)
# scanning.add_command(label="pingSwep", command=funcao3)
menu_arquivo.add_command(label="Escolha a pasta ", command=funcao1)
menu_arquivo.add_command(label="Função 2", command=funcao2)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

# Criar um menu "Ajuda" com uma opção
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=mostrar_sobre)

# Criar uma label para exibir o resultado das funções
resultado_label = tk.Label(janela, text="Resultado aparecerá aqui", padx=10, pady=10)
resultado_label.pack()

janela.mainloop()