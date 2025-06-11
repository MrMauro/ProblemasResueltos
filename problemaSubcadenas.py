# solucion(aaabbbbbbbbbccccccccc) = abc

def subcadena(s):
    if not s:
        return ""

    resultado = s[0]

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            resultado += s[i]

    return resultado

print(subcadena("asddfffffaaaafasaaaaaaa"))
