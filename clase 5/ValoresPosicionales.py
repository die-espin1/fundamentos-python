numero = input("Ingresa un número entero: ")

while not numero.isdigit():
    print("Debes ingresar un número entero que sí sea positivo :D")
    numero = input("Ingresa un número entero: ")

numero = int(numero)
print(f"\nProceso de reducción para {numero}:")

while numero >= 10:
    digitos = str(numero)
    suma = 0
    
    for d in digitos:
        suma += int(d)
  
    print(f"{numero} = {suma}")
    numero = suma

# Mostrar 
print(f"\nEl resultado final es: {numero}")
