from importlib.resources import contents
import os
from cryptography.fernet import Fernet
from tkinter.filedialog import askdirectory

def encrypted():
    origem = askdirectory(title="Pasta Origem")
    print(origem)
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

def decrypted():
    origem = askdirectory(title="Pasta Origem")
    print(origem)
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

# encrypted()  # Se quiser criptografar os arquivos
decrypted()  # Se quiser descriptografar os arquivos
