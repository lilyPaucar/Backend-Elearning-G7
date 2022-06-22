num_ad=int(input("ingrese numero ah adivinar: "))
num=10
while num_ad!=num:
    if num_ad<num:
       print("el numero es mayor que ese")
    elif num_ad>num:
        print("el numero es menor que ese")
    num_ad=int(input("ingrese numero ah adivinar: "))
print("felicitaciones adividaste el numero")