import sys
import os
import platform
import subprocess
from time import sleep
import tkinter as tk
from tkinter import messagebox

# Testando comandos no sistema
# os.environ
os.getcwd()

os.listdir()

os.mkdir("teste")

sleep(5)

os.rmdir("teste")

# Criando interfaces com o tkinter

def funcao1():
    resultado = ""
    for i in range(1, 6):  # Exemplo de um loop de 1 a 5
        resultado += f"Resultado {i}: {i * 2}\n"  # Exemplo de cálculo simples
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
def mostrar_sobre():
    messagebox.showinfo("Sobre", "Este é um exemplo de aplicação com Tkinter.")


janela = tk.Tk()
janela.title("Testando o tk")
janela.geometry("800x300")

# Criar uma barra de menus
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)
# Criar um menu "Arquivo" com duas opções
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Função 1", command=funcao1)
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