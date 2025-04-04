import random
# print() Muestra data en la consola
print("Hello World")
print("1000")
print(True)
# Se pueden imprimir expresiones
print(2 + 2)

# <--- Comentario para documentar
# Variables
aceleracion = 'velocidad / tiempo'
gravedad = 9.8

print(gravedad)

# tipos de datos
# integer
secret_number = 42
# float
pi = 3.14
# string
greting = 'Hiii'
print(len(greting))
# large string
message = """sdasdasdasdasd
asdasdasd
asdasd
"""
# bolean
earth_is_flat = False

# operaciones aritmeticas
# suma
suma = 10 + 12
# resta
rest = 30 - 8
# multiplicacion
product = 24 * 0.75
# division
div = 81 / 9
# modulo
cociente = 76 % 4
# potencia
exp = 2 ** 3

# input() agarra el valor del usuario
username = input("Enter your name: ")
age = int(input("Enter your age: "))

grade = 65
# condiciones
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")

# operadores relacionales
# a == b igual a
# a != b no es igual a
# a < b menor que
# a <= b menor o igual que
# a > b mayor que
# a >= b mayor o igual que

# operadores logicos

# a and b # Verdadero si ambos son verdaderos
# a or b # verdadero si al menos uno es verdadero
# not a # verdaero si a es falso

# random
num = random.randint(1, 9)  # genera un numero aleatorio entre 1 y 9

# loops
# while loop
coffee = random.randint(0, 10)

while (coffee < 1):  # se ejecuta mientras la condicion sea verdadera
    print("tired")

# for loop
for i in range(10):  # se ejecuta 10 veces
    print(i)
