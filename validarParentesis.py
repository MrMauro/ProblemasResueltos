def es_valido(string):
    diccionario={"[":"]","{":"}","(":")"}
    stack=[]

    for char in string:
        if char in diccionario:
            stack.append(char)
        elif char in diccionario.values():
            if not stack:
                return False
            elif diccionario[stack.pop()] != char:  # diccionario["("] = ")"
                return False
    return True
