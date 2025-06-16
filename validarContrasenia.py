# Vamos a validar si una contrasenia es compleja
# - Al menos 8 caracteres
# - Incluye al menos una letra minuscula
# - Incluye al menos una letra mayuscula
# - Incluye al menos un numero
# - Incluye al menos un caracter especial ej (@,#,!,&)

def validar_contrasenia(contrasenia):
    if len(contrasenia)<8:
        print("Contrasenia invalida: Al menos 8 caracteres")
        return False
    elif contrasenia.upper() == contrasenia:
        print("Contrasenia invalida: Al menos una minuscula")
        return False
    elif contrasenia.lower() == contrasenia:
        print("Contrasenia invalida: Al menos una mayuscula")
        return False
    
    contNumero=0
    number = ["1","2","3","4","5","6","7","8","9"]
    for char in contrasenia:
        if char in number:
            contNumero+=1
    
    if contNumero == 0:
        print("Contrasenia invalida: La contrasenia no contiene numeros")
        return False
    
    contCaracteresEspeciales=0
    caracterEspecial = ["@","#","!","&"]
    for char in contrasenia:
        if char in caracterEspecial:
            contCaracteresEspeciales+=1

    if contCaracteresEspeciales == 0:
        print("Contrasenia invalida: La contrasenia no contiene caracteres especiales. ej (@,#,!,&)")
        return False

    print("Contrasenia valida")
    return True

contrasenia=""
while not validar_contrasenia(contrasenia):
    contrasenia = input("Ingrese su contrasenia: ")