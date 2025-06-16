import random

def logica_cpu(matriz):
    while True:
        x = random.randrange(3)
        y = random.randrange(3)
        if matriz[x][y] == "-":
            matriz[x][y] = "o"
            break

def logica_player(matriz):
    while True:
        try:
            x = int(input("Elige la fila (0, 1, 2): "))
            y = int(input("Elige la columna (0, 1, 2): "))
        except ValueError:
            print("Ingresa un numero valido.")
            continue

        if x > 2 or y > 2 or x < 0 or y < 0:
            print("Posicion fuera del rango.")
        elif matriz[x][y] != "-":
            print("Posicion ocupada. Elegir otra")
        else:
            matriz[x][y] = "x"
            break

def verificar_ganador(matriz):
    GANA_PLAYER=0
    GANA_CPU=1
    EMPATE=2

    # conteo en la primera fila
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[i][0] == "x":
            contador_x+=1
        elif matriz[i][0] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo segunda fila
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[i][1] == "x":
            contador_x+=1
        elif matriz[i][1] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo tercera fila
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[i][2] == "x":
            contador_x+=1
        elif matriz[i][2] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo primera columna
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[0][i] == "x":
            contador_x+=1
        elif matriz[0][i] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo segunda columna
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[1][i] == "x":
            contador_x+=1
        elif matriz[1][i] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo tercera columna
    contador_x=0
    contador_o=0
    for i in range(3):
        if matriz[2][i] == "x":
            contador_x+=1
        elif matriz[2][i] == "o":
            contador_o +=1

    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo diagonal principal
    contador_x=0
    contador_o=0

    for i in range(3):
        if matriz[i][i] == "x":
            contador_x+=1
        elif matriz[i][i] == "o":
            contador_o+=1
    
    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU
    # conteo antidiagonal
    contador_x=0
    contador_o=0
    
    for i in range(3):
        if matriz[2-i][i] == "x":
            contador_x+=1
        elif matriz[2-i][i] == "o":
            contador_o+=1
    
    if contador_x==3:
        return GANA_PLAYER
    elif contador_o==3:
        return GANA_CPU

    # Verificar si aún hay espacios vacíos
    for fila in matriz:
        if "-" in fila:
            return None  # No hay ganador ni empate aún
    return EMPATE

def imprimir_tiktaktoe(matriz):
    for fila in matriz:
        print(" ".join(fila))

tiktaktoe = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]
HAY_GANADOR = False
estado = 0
print("-----------")
print("TIK TAK TOE")
print("-----------")
while not HAY_GANADOR:    
    imprimir_tiktaktoe(tiktaktoe)
    logica_player(tiktaktoe)
    logica_cpu(tiktaktoe)

    if verificar_ganador(tiktaktoe) == 0 or verificar_ganador(tiktaktoe) == 1 or verificar_ganador(tiktaktoe) == 2:
        HAY_GANADOR = True

if verificar_ganador(tiktaktoe) == 0:
    imprimir_tiktaktoe(tiktaktoe)
    print("Ganaste!!")
elif verificar_ganador(tiktaktoe) == 1:
    imprimir_tiktaktoe(tiktaktoe)
    print("Suerte para la proxima.")
else:
    imprimir_tiktaktoe(tiktaktoe)
    print("Empate.")