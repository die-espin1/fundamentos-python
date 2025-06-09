'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Juego Del entorno
Descripción: Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una matriz binaria cuántos elementos con valor 1 hay en las celdas vecinas.
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]
'''

N = int(input())
M = int(input())

matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

# Crear una matriz de resultados inicializada con ceros
resultado = [[0 for _ in range(M)] for _ in range(N)]

# Definir las 8 direcciones posibles de los vecinos
direcciones = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1),  (1, 0), (1, 1)]

# Iterar sobre cada celda de la matriz
for i in range(N):
    for j in range(M):
        suma = 0
        # Verificar cada vecino posible
        for di, dj in direcciones:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                suma += matriz[ni][nj]
        resultado[i][j] = suma

for fila in resultado:
    print(fila)