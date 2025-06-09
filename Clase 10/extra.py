'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Identificando islas
Descripción: Dada una matriz cuadrada ingresada por el usuario, cuenta la cantidad de islas disponibles.
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

visitados = [[False for _ in range(M)] for _ in range(N)]
contador = 0

# Definir direcciones posibles (arriba, abajo, izquierda, derecha)
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS iterativo
pila = []

# Recorrer toda la matriz
for i in range(N):
    for j in range(M):
        if matriz[i][j] == 1 and not visitados[i][j]:
            contador += 1
            visitados[i][j] = True
            pila.append((i, j))
            
            while pila:
                x, y = pila.pop()
                # Explorar vecinos
                for dx, dy in direcciones:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if matriz[nx][ny] == 1 and not visitados[nx][ny]:
                            visitados[nx][ny] = True
                            pila.append((nx, ny))

print(contador)