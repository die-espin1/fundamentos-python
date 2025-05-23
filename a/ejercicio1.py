password = input("Ingresa una contraseña: ")

tiene_numero = False
tiene_mayuscula = False

if len(password) >= 8:
    for caracter in password:
        if caracter >= '0' and caracter <= '9':
            tiene_numero = True
        if caracter >= 'A' and caracter <= 'Z':
            tiene_mayuscula = True

    if tiene_numero and tiene_mayuscula:
        print("Contraseña segura")
    else:
        print("Contraseña no segura")
else:
    print("Contraseña no segura")
