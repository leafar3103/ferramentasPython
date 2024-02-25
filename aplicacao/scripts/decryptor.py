import os
from cryptography.fernet import Fernet
from tkinter.filedialog import askdirectory

class Decryptor:
    def __init__(self):
        pass

    def decrypt(self, origem):
        files = []
        arquivos = os.listdir(origem)

        with open("chave.key", "rb") as chave:
            key = chave.read()

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
                conteudo_encrypted = arquivo.read()
            conteudo_decrypted = Fernet(key).decrypt(conteudo_encrypted)
            with open(file, "wb") as arquivo:
                arquivo.write(conteudo_decrypted)
