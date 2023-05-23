numeros = [10,30,50,100,255,500]
#append = Agrega un objeto en la ultima posicion 
numeros.append(1000)
print(numeros)

extra = [75,350,999]
#extend = agrega un arreglo al fianl de nuestra lista
numeros.extend(extra)
print(numeros)

#insert = agrega un valor en posicion especifica y mueve la lista a ña derecha.
numeros.insert(6,5000)
print(numeros)

#remove = le entrego un valor, ese valor se busca en la lista y se elimina
#Se debe ingresar el valor, no la posicion
numeros.remove(50)
print(numeros)

#pop = elimina la posicion del numero
numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)

#reverse = invierte el orden de la lista
numeros.reverse()
print(numeros)

#sort = Ordena los valores de menor a mayor
numeros.sort()
print(numeros)

#sort(reverse=true) = Odena los valores de mayor a menor
numeros.sort(reverse=True)
print(numeros)

