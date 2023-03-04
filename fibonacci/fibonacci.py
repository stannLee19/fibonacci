# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# numero = int(input("Ingresa un número para calcular su factorial: "))

# if numero < 0:
#     print("No se puede calcular el factorial de un número negativo.")
# elif numero == 0:
#     print("El factorial de 0 es 1.")
# else:
#     print("El factorial de", numero, "es", factorial(numero))

def factorial():
    n = int (input("ingrese  un numero entero:"))
result =  1
for i in range (1, n+1):
    result *= i
    return result