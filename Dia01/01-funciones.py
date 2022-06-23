from sre_constants import RANGE


def saludar():
    print("buenas tardes!")
saludar()

def saludarConNombre(nombre):
    print(nombre)
saludarConNombre("lily")

def saludarConNombre(nombre):
    print("hola {}, como te va?".format(nombre))
saludarConNombre("lily")

def calcularIGV(valor):
    """funcion que recibe el valor y te devuelve el valor incluido su IGV"""
    valorIncluidoIGV=valor*1.18
    return valorIncluidoIGV

precio=100
precioConIGV=calcularIGV(precio)
print(precioConIGV)

def calcularSalarioMinimo(profesion, experiencia):
    salarioMinimo=1050
    if profesion=="desarrollador":
       if experiencia=="basica":
            salarioMinimo=3000
       elif experiencia=="media":
            salarioMinimo=4800
       elif experiencia=="avanzada":
            salarioMinimo=7000
    if profesion=="marketing":
       if experiencia=="basica":
            salarioMinimo=2500
       elif experiencia=="media":
            salarioMinimo=4150
       elif experiencia=="avanzada":
            salarioMinimo=6820
    return salarioMinimo

profesion, experiencia= "desarrollador","media"
salario=calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia= "desarrollador","basica"
salario=calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia= "marketing","media"
salario=calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia= "astronauta","media"
salario=calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia= "basica","marketing"
salario=calcularSalarioMinimo(profesion, experiencia)
print(salario)

electrodomesticos =[]
def registrarElectrodomesticos(nombre,precio, almacen="las malvinas"):
    electrodomesticos.append({"nombre":nombre,"precio":precio,"almacen":almacen})
    return True
registrarElectrodomesticos("licuadora 12v", 115.00)
registrarElectrodomesticos("freidora de aire", 100, "cercado")
registrarElectrodomesticos("secador de cabello",140)
print(electrodomesticos)

def contarElectrodomesticosPorAlmacen():
    """cuenta cuantos electrodomesticos hay en cada almacen"""
    malvinas=0
    cercado=0
    otro=0
    for electrodomestico in electrodomesticos:
        if electrodomestico["almacen"]=="las malvinas":
            malvinas+=1
        if electrodomestico["almacen"]=="cercado":
            cercado+=1
        else:
            otro=+1
    print("en la malvinas hay {}, en el cercado hay {} y en otros hay {} electrodomesticos".format(malvinas,cercado,otro))
contarElectrodomesticosPorAlmacen()

def contarElectrodomesticosPorAlmacen():
    """cuenta cuantos electrodomesticos hay en cada almacen"""
    malvinas=0
    cercado=0
    otro=0
    for electrodomestico in electrodomesticos:
        if electrodomestico["almacen"]=="las malvinas":
            malvinas+=1
        if electrodomestico["almacen"]=="cercado":
            cercado+=1
        else:
            otro=+1
    return[malvinas, cercado,otro]

resultado= contarElectrodomesticosPorAlmacen()
print("en la malvinas hay {}, en el cercado hay {} y en otros hay {} electrodomesticos".format(resultado[0],resultado[1],resultado[2]))

#si en una funcion queremos recibir un numero indeterminado de valores

def recibirAlumnos(*alumnos):
    #cuando un parametro tiene el * al comienzo significa que ese parametro recibira  n valores y la convertira en una tupla, solo t acepta 1 paramatro con ese tipo
    print(type(alumnos))
    print(alumnos)