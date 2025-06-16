# Vamos a validar si una contrasenia es compleja
# - Al menos 8 caracteres
# - Incluye al menos una letra minuscula
# - Incluye al menos una letra mayuscula
# - Incluye al menos un numero
# - Incluye al menos un caracter especial ej (@,#,!,&)

def validar_contrasenia(contrasenia):
    if len(contrasenia)<8:
        return "Contrasenia invalida: Al menos 8 caracteres"
    elif contrasenia.upper() == contrasenia:
        return "Contrasenia invalida: Al menos una minuscula"
    elif contrasenia.lower() == contrasenia:
        return "Contrasenia invalida: Al menos una mayuscula"
    
    contNumero=0
    number = ["1","2","3","4","5","6","7","8","9"]
    for char in contrasenia:
        if char in number:
            contNumero+=1
    
    if contNumero == 0:
        return "Contrasenia invalida: La contrasenia no contiene numeros"
    
    contCaracteresEspeciales=0
    caracterEspecial = ["@","#","!","&"]
    for char in contrasenia:
        if char in caracterEspecial:
            contCaracteresEspeciales+=1

    if contCaracteresEspeciales == 0:
        return "Contrasenia invalida: La contrasenia no contiene caracteres especiales"

    return "Contrasenia Valida"

contrasenia="ASDASDA123@SDAaaa"
print(validar_contrasenia(contrasenia))