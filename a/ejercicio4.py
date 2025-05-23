n = int(input("Ingresa un número: "))

if 1 <= n <= 10**18:
    if n % 7 == 0 and n % 5 != 0:
        print("Mágico")
    else:
        print("Normal")
else:
    print("Número fuera del rango permitido (1 ≤ n ≤ 10^18)")
