# Un numero es perfecto si sus divisores propios suman al número
# Ejm: 6 es perfecto porque sus divisores son {1,2,3,6} y 6 = 1 + 2 + 3

def imprimirNumerosPerfectos(n: int):
    
    for j in range(1,n):
        divisores=[]
        for i in range(1,j):
            if j % i == 0:
                divisores.append(i)

        sumaDivisores=0
        for divisor in divisores:
            sumaDivisores+=divisor
        if sumaDivisores==j:
                print(j)

imprimirNumerosPerfectos(10000)