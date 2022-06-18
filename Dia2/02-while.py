from random import random


numero =10
while numero>0:
    print("numero positivo")
    print(numero)
    numero -=1
#solicitar 5 digitos para la loteria pero estos no pueden ser mayor que 100 ni numero negativos

cont=0
while cont<5:
    numero=int(input("ingrese numero"))
    if numero <100 and numero >0:
       cont+=1
       continue
    print("numero incorecto, vuelve a intentar")
