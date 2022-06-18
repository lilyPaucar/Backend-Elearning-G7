from operator import length_hint


numeros=[10,20,30,40,50,60]
for numero in numeros:
    print(numero)
frase_motivadora="al que madruga, encuentra todo cerrado"
contador =0
for caracter in frase_motivadora:
    #cuentame cuantas letras n hay en la frase
    if caracter == "n":
       contador +=1
print("hay {} veces repetida la letra n".format(contador))

for valor in range(10):
    #empezara desde 0 hasta < 10 e incrementara de 1 en 1
    print(valor)
for valor in range(3,7):
    #inicia en 3 y termina <7 incremetandose de 1 en 1
    print(valor)
for valor in range (4,7,2):
    #inicia en 4 y termina en < 7 y se incremetara de 2 en 2
    print(valor)

numeros =[10,30,12,17,24,67]
#cuantos numeros son numeros pares y cuantos multiplos de 3
contador=0
contador1=0
for numero in numeros:
    print(numero)
    if numero%2 ==0:
        contador+=1
    if numero%3==0:
        contador1+=1
print("hay {} numeros pares".format(contador))
print("hay {} numeros multiplos de 3".format(contador1))

# supongamos que los 10000 son los usuarios en un sistema y queremos encontrar al usuario con un determinado nombre (y ese usuario es el numero 600)for valor in range(o)
for valor in range(0,10000):
    print (valor)
    if (valor ==600):
        print("el usuario fue encontrado")
        #el break sirve para finalizar de manera prematura un bucle
        break

for valor in range(0,20):
    if (valor ==5):
        print("el usuario fue encontrado")
        #el continue sirve para continuar los numeros del bucle despues de imprimir el resultado de la condicion
        continue
    print (valor)

for valor in range(0,20):
    # TODO:implementar la logica
    #pass no hara nada pero evitara que nos lance error python
    pass

alumnos =["eduardo","lily","jose","rafael"]

for alumno in alumnos:
   if alumno =="eduardo":
        print(alumno)
        break   
else:
    #ingresara una vez haya perminado de iterar el for
    print("no se encontro el alumno")
