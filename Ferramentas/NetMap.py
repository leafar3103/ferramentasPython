#!usr/bin/python
import sys 
import os

rede = "192.168.0."
encontrado = []

for ip in range(18,22):
    address = rede+str(ip)
    response = os.system("ping -c 1 " + rede+str(ip))  
    if response == 0:
        print (f"\n\n O host é: {address} \n")
        encontrado = address
    else:
        print("\n") 
print(f"""         ##############################################
         #      o Ip encontrado é:  {encontrado}      #
         ##############################################
""")