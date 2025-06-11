def suma_no_repetido(lista):
    frecuencia={}
    for i in lista:
        if i not in frecuencia:
            frecuencia[i]=1
        else:
            frecuencia[i]+=1
    suma=0
    for i in frecuencia:
        if frecuencia[i] < 2:
            suma += i
    return suma
entrada = [1, 2, 2, 3, 4, 1, 5]
print(suma_no_repetido(entrada))