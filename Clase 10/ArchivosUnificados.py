'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Diagonal principal y secundaria
Descripción: Dada una matriz cuadrada ingresada por el usuario, crea 2 listas, una con los elementos de la diagonal principal y otra con los elementos de la diagonal
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]


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

'''


'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Matriz Simétrica y no simétrica
Descripción: Dada una matriz cuadrada ingresada por el usuario, comprueba si la matriz cuadrada es simétrica respecto a su diagonal principal y otra con los elementos de la diagonal
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]


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

'''

'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Juego Del entorno
Descripción: Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una matriz binaria cuántos elementos con valor 1 hay en las celdas vecinas.
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]


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
'''


'''
Clase:        Clase 11
Tema:         Manejo de listas
Ejercicio:    Identificando islas
Descripción: Dada una matriz cuadrada ingresada por el usuario, cuenta la cantidad de islas disponibles.
Autor:        Diego René Espinoza Díaz
Fecha:        2025-06-09
Estado:       [ Terminado ]


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

print(contador)'''