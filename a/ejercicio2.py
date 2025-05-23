elementos = int(input("Ingrese los elementos consumidos: "))

if elementos <= 100:
    impuesto = 0
elif elementos <= 200:
    impuesto = (elementos - 100) * 0.5
else:
    impuesto = (100 * 0.5) + ((elementos - 200) * 0.7)

# Mostrar el resultado
print("Impuesto aplicado: $", impuesto)
