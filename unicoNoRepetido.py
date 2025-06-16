# operador XOR: a ^ a = 0
#               a ^ 0 = a

def unico_no_repetido(lista):
    resultado=0
    for num in lista:
        resultado^=num

    return resultado