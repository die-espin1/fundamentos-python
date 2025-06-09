'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Diagonal principal y secundaria
Descripción: Dada una matriz cuadrada ingresada por el usuario, crea 2 listas, una con los elementos de la diagonal principal y otra con los elementos de la diagonal
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]
'''

n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []

# Leer los valores de la matriz
print("Ingrese las filas de la matriz (valores separados por comas):")
for _ in range(n):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

# Extraer las diagonales
diagonal_principal = []
diagonal_secundaria = []

for i in range(n):
    diagonal_principal.append(matriz[i][i])
    diagonal_secundaria.append(matriz[i][n - 1 - i])

# Mostrar resultados
print(diagonal_principal)
print(diagonal_secundaria)
