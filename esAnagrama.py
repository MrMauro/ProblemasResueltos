# Una palabra es anagrama si:
# es_anagrama("Roma ","Amor") -> return True
# es_anagrama(" Messi","Mbappe") -> return False

def es_anagrama(palabra1,palabra2):
    # hago todo minusculas
    palabra1=palabra1.lower()   
    palabra2=palabra2.lower()
    # quito los espacios
    palabra1=palabra1.replace(" ","")
    palabra2=palabra2.replace(" ","")

    frecuencia1={}
    frecuencia2={}

    for char in palabra1:
        if char not in frecuencia1: # aparece por primera vez
            frecuencia1[char]=1
        else:  # if char in frecuencia1: se repite
            frecuencia1[char]+=1

    for char in palabra2:
        if char not in frecuencia2: # aparece por primera vez
            frecuencia2[char]=1
        else:  # if char in frecuencia2: se repite
            frecuencia2[char]+=1

    return frecuencia1 == frecuencia2

print(es_anagrama("mEssi","essim"))
print(es_anagrama("Roma"," am or"))
print(es_anagrama("newima","asd"))