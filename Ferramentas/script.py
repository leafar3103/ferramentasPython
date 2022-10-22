#!/usr/bin/python
from lib2to3.pgen2.token import MINEQUAL
import socket

ip = "192.168.0.19"
porta = 445
meuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = meuSocket.connect_ex((ip,porta))

if (res == 0 ):
    print ("Porta Aberta")
else:
    print ("Porta Fechada")