# tuplas son datos ordenados PERO no editables
profesores=("eduardo","osmar")
print(profesores[0])

#profesores="ximena"
#prosfesores.append("raul")

data =(1,True, "Junio", 14.5,[1,2,3,4])

print(data[1:4])

#se puede eleiminar toda la pvariable pero no se puede eliminar parte del contenido de la tupla

del data

notas=(10,15,15,18,10,5,7,14)
#count sirve para contar las veces que se repite cierto valor 
print(notas. coun(10))
print(notas.count(20))
print(notas.count("onomatopeya"))

#index si existe ese valor en la tupla me retornara la posicion en la que se encuentra, sino existe me emitira error

print(notas.index(15))