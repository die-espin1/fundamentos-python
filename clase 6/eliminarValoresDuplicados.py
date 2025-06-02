# Leer la entrada
entrada = input("Ingresa los números separados por espacios: ")
numeros = list(map(int, entrada.split()))

vistos = set()
resultado = []

# Procesar sin usar funciones
for numero in numeros:
    if numero not in vistos:
        resultado.append(numero)
        vistos.add(numero)

# Imprimir el resultado
for i in range(len(resultado)):
    print(resultado[i], end=' ')
