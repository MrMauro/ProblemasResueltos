# Two sum: lista: [2,5,8,11], objetivo 10: return {0,2}

def twoSum(lista,objetivo: int):
    for i in range (len(lista)):
        for j in range (i+1,len(lista)):
            if(lista[i] + lista[j] == objetivo):
                resultado = {i,j}

    return resultado

def twoSum(lista, objetivo: int):    # Usando hashmap
    vistos = {}  # diccionario: valor -> índice

    for i, num in enumerate(lista):
        complemento = objetivo - num
        if complemento in vistos:
            return (vistos[complemento], i)
        vistos[num] = i

    return None


print(twoSum([4,5,6,7,8,9],10))