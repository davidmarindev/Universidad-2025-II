# Tipos de datos
# Variables
# Operadores
# Condicionales
# Ciclos 
# Funciones
# Metodos
# Estructuras de datos
# Manejo de archivos

# Tipos de datos simples

# String
# Int
# Float
# Boolean
# None

# Tipos de datos compuestos

# Lista
# Tupla
# Diccionario
# Set

name = "Pedro"

print(type(name))

name = "Juan"

print(name)

name = 123

print(type(name))


# Operadores aritméticos
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
h = a % b
i = a ** b

# Operadores de comparación
x = 5
y = 10

is_equal = x == y
is_not_equal = x != y
is_greater = x > y
is_less = x < y
is_greater_equal = x >= y
is_less_equal = x <= y

var_a = 15
var_b = 20
var_c = 10

print("Condicion 1:", var_a > var_b)
print("Condicion 2:", var_b < var_a)
print("Condicion 3:", var_a != var_b)

# Operadores lógicos

# and
# or
# not

print("Operador AND:", (var_a < var_b) and (var_a > var_c))
print("Operador OR:", (var_a > var_b) or (var_a != var_c))
print("Operador NOT:", not(var_a > var_b))

# Operadores de asignación
var_d = 30
var_d += 5
var_d -= 3
var_d *= 2
var_d /= 4
print("Nuevo valor de var_d:", var_d)

# i++  # No es válido en Python

i += 1  # Forma correcta de incrementar en Python

mes = 1

if mes == 1 or mes.lower() == "enero":
    print("Enero tiene 31 días.")
elif mes == 2:
    print("Febrero tiene 28 días.")
elif mes == 3:
    print("Marzo tiene 30")
else:
    print("Mes no válido")
    
# nuevo_mes = int(input("Ingresa un numero:"))

# match nuevo_mes:
#   case 1: 
#     print("Enero")
#   case 2:
#     print("Febrero")
#   case _:
#     print("Mes no valido")
    
    
for i in range(1, 101, 2):
    print("Iteración:", i)
    
# 10000001 -> byte

palabra = "Python"

print("Longitud de la palabra:", len(palabra))
print("Palabra", palabra[0])

for letra in palabra:
    print("Letra:", letra)

# for(i=0 i< len(palabra); i++):
#     print("Letra:", palabra[i])

lista_numeros = [1, 2, 3, 4, 5]

print(lista_numeros[3])

# map in python list
nueva_lista = list(map(lambda x: x * 2, lista_numeros))

print("Nueva lista usando map():", nueva_lista)

for numero in lista_numeros:
    numero *= 2
    
persona = {
  "nombre": "Ana",
  "edad": 28,
  "ciudad": "Madrid",
  "direccion": {
      "calle": "Calle Falsa 123",
      "codigo_postal": "28080"
   },
  "telefonos": ["123456789", "987654321"]
}

personas = [
  persona, 
  {
  "nombre": "Pedro",
  "edad": 30,
  "ciudad": "Madrid",
  "direccion": {
      "calle": "Calle Falsa 123",
      "codigo_postal": "28080"
   },
  "telefonos": ["123456789", "987654321"]
  },
  {
  "nombre": "Juan",
  "edad": 28,
  "ciudad": "Barcelona",
  "direccion": {
      "calle": "Calle Falsa 125",
      "codigo_postal": "28080"
   },
  "telefonos": ["123456789", "987654321"]
}]

print(len(personas))

for p in personas:
  if p["ciudad"] == "Madrid":
    print("Persona:", p["nombre"])
    
frase = "Hola como estas?"

arr = frase.split(" ")

print(arr)

string_new = ",".join(arr)

print(string_new)