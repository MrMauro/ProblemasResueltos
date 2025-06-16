# Vamos a contar las vocales de una fraase.
# - Valen mayusculas y minusculas


def contar_vocales(frase):
    frase = frase.lower()

    listaVocales = ['a','e','i','o','u']
    contVocales=0

    for char in frase:
        if char in listaVocales:
            contVocales+=1
    return contVocales

frase = "Programacion es divertida"
print(f"La frase \"{frase}\" tiene {contar_vocales(frase)} vocales.")
