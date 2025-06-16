# contar los elementos unicos en una lista

def contar_elementos_unicos(lista):
    if not lista:
        return 0
    listaAux=[]
    for i in lista:
        if i not in listaAux:
            listaAux.append(i)
    return len(listaAux)

lista = [1,2,2,3,4,4,5,6,7,7,56]
print(f"La lista tiene {contar_elementos_unicos(lista)} elementos unicos.")