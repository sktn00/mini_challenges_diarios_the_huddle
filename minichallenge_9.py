# Recursión Factorial: Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5)

def recursion_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursion_factorial(num - 1)
    
print(recursion_factorial(7))