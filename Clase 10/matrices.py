lista = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

#acceder a una lista
lista[0]

fila = lista[2]
fila[1]
#10

#Recorrer una matriz, for anidado
"""for fila in lista:
    for celda in fila:
        print(f"{celda}", end ="")
    print()"""

for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(f"{lista[i][j],}", end="")
    print()

        
    