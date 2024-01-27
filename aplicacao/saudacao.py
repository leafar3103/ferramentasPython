# modulo_classe.py
import tkinter as tk
import tkinter.simpledialog as sd
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        return f"Olá, {self.nome}! Esta é uma mensagem da classe do módulo."
    
    def obter_nome_do_usuario(self):
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal
        novo_nome = tk.simpledialog.askstring("Nome", "Digite seu nome:")
        root.destroy()  # Destroi a janela personalizada

        if novo_nome:
            self.nome = novo_nome