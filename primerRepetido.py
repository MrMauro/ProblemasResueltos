def primer_repetido(cadena):
    cadena=cadena.lower()
    frecuencias={}
    for char in cadena:
        # se usa la cadena de frecuencias
        if char not in frecuencias:
            frecuencias[char]=1
        elif char in frecuencias:
            frecuencias[char]+=1
        # si la frecuencia del char es 2, retorna al char
        if frecuencias[char]>1:
            return char
        
    return ""

entrada = "abcdefgabc"
print(primer_repetido(entrada))
entrada = "python"
print(primer_repetido(entrada))
