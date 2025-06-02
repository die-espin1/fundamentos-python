# ejercicio de valores duplicados
elementosVistos = set()
resultadoFinal = []

entrada = list(map(int, input("Ingresa los números separados por espacio: ").split()))

for numero in entrada:
    if numero not in elementosVistos:
        resultadoFinal.append(numero)
        elementosVistos.add(numero)

print(" ".join(map(str, resultadoFinal)))
