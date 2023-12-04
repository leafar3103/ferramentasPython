import os
from time import sleep
import tkinter as tk

# Testando comandos no sistema
# os.environ
os.getcwd()

os.listdir()

os.mkdir("teste")

sleep(5)

os.rmdir("teste")

# Criando interfaces com o tkinter

janela = tk.Tk()
janela.title("Testando o tk")

janela.mainloop()