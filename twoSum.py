# Two sum: lista: [2,5,8,11], objetivo 10: return 0,8

def twoSum(lista,objetivo):
    for i in range (len(lista)):
        for j in range (i+1,len(lista)):
            if(lista[i] + lista[j] ==objetivo):
                resultado = {i,j}

    return resultado

print(twoSum([4,5,6,7,8,9],10))