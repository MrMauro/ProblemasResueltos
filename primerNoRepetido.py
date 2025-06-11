def primer_no_repetido(cadena):
    diccionario={}
    for i,l in enumerate(cadena):
        if l in diccionario:
            #logica si el char esta en el diccionario
            diccionario[l]=-1
        else:
            diccionario[l]=i
    for l in cadena:
        if diccionario[l] != -1:
            return l
        
    return ""

print(primer_no_repetido("aadhdafjsdhjrj"))
