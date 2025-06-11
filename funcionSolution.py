# 4 -> 2 -> 1       3 pasos
# 15 -> 16 -> 8 -> 4 -> 2 -> 1      5 pasos

def sol(num: int):
    count = 0
    while num!=1:  # mientras el numero sea distinto (!=) de 1
        if num%2==0: # si es par
            num=num/2 # el numero se divide en 2
            count+=1  # cuento 1 paso
        else:         # si es impar
            num+=1    # el numero aumenta en 1
            count+=1  # cuento un paso
    return count

print(f"El número 1378126784 tiene {sol(1378126784)} pasos.")

