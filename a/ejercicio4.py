#
import random

valor_oculto = random.randint(1, 100)
total_pruebas = 0

print("¡Reto de Adivinanzas!")
print("Tengo escondido un valor del 1 al 100. ¿Serás capaz de descubrirlo?")

while True:
    try:
        propuesta = int(input("Escribe tu propuesta (1-100): "))
        total_pruebas += 1
      
        if propuesta < 1 or propuesta > 100:
            print("El valor debe estar entre 1 y 100. Intenta nuevamente.")
            continue
        
        if propuesta < valor_oculto:
            print("El valor buscado es más alto")
        elif propuesta > valor_oculto:
            print("El valor buscado es más bajo")
        else:
            print(f"¡LO ENCONTRASTE! El número era {valor_oculto}")
            print(f"Total de intentos: {total_pruebas}")
            print("¡Juego terminado!")
            break
    except:
        print("Debes ingresar un número entero válido")
