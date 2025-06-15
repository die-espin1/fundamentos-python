"""
Crear una función que cuente recursivamente los vecinos en una matriz binaria
Condición: Contar vecinos que se encuentre horizontal y verticalmente
"""

def contar_vecinos(matriz, fila, columna, visitados=None):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    if visitados is None:
        visitados = [[False for _ in range(columnas)] for _ in range(filas)]

    # Validar límites y si ya fue visitado o no es un 1
    if (fila < 0 or fila >= filas or
        columna < 0 or columna >= columnas or
        matriz[fila][columna] == 0 or
        visitados[fila][columna]):
        return 0

    # Marcar como visitado
    visitados[fila][columna] = True

    cuenta = 1
    cuenta += contar_vecinos(matriz, fila - 1, columna, visitados)  
    cuenta += contar_vecinos(matriz, fila + 1, columna, visitados)  
    cuenta += contar_vecinos(matriz, fila, columna - 1, visitados)  
    cuenta += contar_vecinos(matriz, fila, columna + 1, visitados)  

    return cuenta
