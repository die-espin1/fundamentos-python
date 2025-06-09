'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Matriz Simétrica y no simétrica
Descripción: Dada una matriz cuadrada ingresada por el usuario, comprueba si la matriz cuadrada es simétrica respecto a su diagonal principal y otra con los elementos de la diagonal
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]
'''

# Leer la dimensión de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []

# Leer las filas de la matriz
print("Ingrese las filas de la matriz (números separados por comas):")
for _ in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

# Imprimir
if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
