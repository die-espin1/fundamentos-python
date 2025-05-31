#ejercicio de números líderes
numeros = list(map(int, input().split()))

if not numeros:
    print()
else:
    max_derecha = numeros[-1]
    lideres = [max_derecha]
    
    for i in range(len(numeros)-2, -1, -1):
        if numeros[i] > max_derecha:
            max_derecha = numeros[i]
            lideres.append(max_derecha)
            
    lideres = lideres[::-1]
    print(' '.join(map(str, lideres)))
