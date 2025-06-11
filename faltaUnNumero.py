# lista = [1,2,3,5] -> return 4 len(lista)=4
def falta(lista):
    temp=[]
    for i in lista:
        if (i-1 or i+1) not in lista:
            if i-1!=0:
                return i-1
            elif i+1!=len(lista+2):
                return i+1

def falta_con_suma(lista):
    suma_enteros:int
    n=len(lista)+1
    suma_enteros=n*(n+1)/2 # suma de los naturales hasta el n
    suma_lista:int
    suma_lista=0
    for i in lista:
        suma_lista+=i
    return suma_enteros-suma_lista

prueba=[1,2,3,4,6,7]
print(falta(prueba))
print(falta_con_suma(prueba))