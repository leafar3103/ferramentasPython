import os
from cryptography.fernet import Fernet
from tkinter.filedialog import askdirectory

class Encryptor:
    def __init__(self):
        pass

    def encrypt(self, origem):
        files = []
        arquivos = os.listdir(origem)

        key = Fernet.generate_key()
        with open("chave.key", "wb") as chave:
            chave.write(key)

        for file in arquivos:
            print(file)
            if file == "crypto.py" or file == "chave.key" or file == "decrypt.py":
                continue
            if os.path.isfile(os.path.join(origem, file)):
                print(file)
                files.append(os.path.join(origem, file))
        print(files)

        for file in files:
            with open(file, "rb") as arquivo:
                conteudo = arquivo.read()
            conteudo_encrypted = Fernet(key).encrypt(conteudo)
            with open(file, "wb") as arquivo:
                arquivo.write(conteudo_encrypted)
