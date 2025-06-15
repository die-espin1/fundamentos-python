import time
#Colocar del 5... 4... 3...
def cuenta_regresiva_iterativa(n):
    for i in range(n, 0, -1):
        print(i, end = "...")
    print("Despegue")
    time.sleep(0.5)
cuenta_regresiva_iterativa(10)


def cuenta_regresiva_recursiva(n):
    #1° Tener en cuenta la condición de parada
    if n <= 0:
        print("¡Despegue!")
    else:
        print(n, end="... ")
        time.sleep(0.5)
        cuenta_regresiva_recursiva(n-1)

cuenta_regresiva_recursiva(10)


#Crear dos funciones (iterativa y recursiva) que genere y devuelva el abecedario
def generar_alfabeto_iterativo():
    alfabeto = ''
    for i in range(26):  # Hay 26 letras en el abecedario inglés
        alfabeto += chr(ord('a') + i)
        alfabeto = alfabeto.rstrip(',')
    return alfabeto
print(generar_alfabeto_iterativo())


def generar_alfabeto_recursivo():
    #1° Tener en cuenta la condición de parada
    if letra == 'z':
        return 'z'
    else:
        return letra + ", " + generar_alfabeto_recursivo(chr(ord(letra) + 1))
print(generar_alfabeto_recursivo())


#Determinar el factorial de un número
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recursivo(n-1)
    
print(factorial_recursivo(5))


