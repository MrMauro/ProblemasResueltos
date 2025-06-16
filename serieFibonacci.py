def fibonacci(n: int):
    if n<0:
        return -1
    elif n==0 or n == 1:
        return 1
    else:        
        return fibonacci(n-2) + fibonacci(n-1)

for i in range(-1,51):
    print(fibonacci(i))