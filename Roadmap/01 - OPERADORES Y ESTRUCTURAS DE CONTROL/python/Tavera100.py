# Operadores Aritmeticos
suma = 2 + 3
resta = 9 - 5
producto = 5 * 5
division = 21 / 7
modulo = 16 % 3
potencia = 8 ** 3
division_entera = 16 // 5
#  Mostrar por pantalla operaciones aritméticas
print('Suma: ', suma)
print('Resta: ', resta)
print('Producto: ' , producto)
print('Division: ', division)
print('Modulo: ', modulo)
print('Potencia: ', potencia)
print('Division con enteros: ', division_entera) 

"""
from random import randint
n1 = randint(1,10)
n2 = randint(1,10)
otra forma de crear variables aleatorias
"""

# Operadores aritmeticos
print(f'Suma {n1} + {n2} = {n1+n2}')
print(f'Resta {n1} - {n2} = {n1-n2}')
print(f'Multiplicacion {n1} * {n2} = {n1*n2}')
print(f'Division {n1} / {n2} = {n1/n2}')
print(f'Resto {n1} % {n2} = {n1%n2}')
print(f'Potencia {n1} ** {n2} = {n1**n2}')
print(f'Division entera {n1} // {n2} = {n1//n2}')
print(f'Suma {n1} + {n2} = {n1+n2}')

# Operadores Relacionales
mayor_que = 3 > 5
menor_que = 5 < 8
igualdad = 7 == 7
mayor_igual = 5 >=5
menor_igual = 7 <= 4
desigualdad = 8 != 6

# Mostrar por pantalla operadores relacionales
print('Mayor que: ', mayor_que)
print('Menor que: ', menor_que)
print('Igualdad: ', igualdad)
print('Mayor o igual que: ', mayor_igual)
print('Menor o igual que: ', menor_igual)
print('Desigualdad: ', desigualdad)


# Operadores Bit a Bit
print('AND', 10 & 12)
print('OR', 10 | 12)
print('XOR', 10 ^ 12)
print('NOT', ~12)
print('Desplazamiento a la derecha', 10 >> 12)
print('Desplazamiento a la izquierda', 10 << 12)


""" Operadores de Asignacion
a = 5
print(f'Operador a = 5 ->{a}')
a += 5
print(f'Operador a += 5 ->{a}')
a -= 5
print(f'Operador a -= 5 ->{a}')
a *= 3
print(f'Operador a *= 3 ->{a}')
a /= 3
print(f'Operador a /= 3 -> {a}')
a %=3
print(f'Operador a %= 3 -> {a}')
a **=3
print(f'Operador a **= 3 -> {a}')
a //=3
print(f'Operador a //= 3 -> {a}')
"""

# Estos operadores son una forma mas rapida de utilizar los operadores Aritmeticos

# Asignacion
x =  0 
print(x)
# Suma
x +=  5
print(x)
# Resta
x -= 5
print(x)
# Producto
x *= 5
print(x)
# Division
x /= 5
print(x)
# Modulo
x %= 5
print(x)
# Potencia
x **= 5
print(x)
# Division Entera
x //= 5
print(x)


# Operadores Logicos
true_value = True
false_value = False
# and - Devuelve true si ambos son True
print('and: ', true_value and false_value)
# or - Devuelve Truse si alguno es False
print('or: ', true_value or false_value)
# not - Devuelve True si alguno es False
print('not: ', not false_value)


# Operadores de Pertenencia
list = [1, 2, 3, 4, 5]
hello = 'Hello World'
# in - Devuelve True si el elemento se encuentra en la lista
print('In list: ', 3 in list)
print('In Hello: ', 'World' in list)
# not in - Devuelve Truse si el elemento NO se encuentra en la lista
print('Not in list: ', 7 not in list)
print('Not in Hello: ', 'Hello' not in list)

"""
# Operadores de identidad
a = 3
b = 3
c = 4
print(f'3 is 3 -> {a is b}')
print(f'4 is not 3 -> {c is not b}')
"""

# Operadores de Identidad
# is - Devuelve True si los operandos se refieren al mismo objeto
# is not - Devuelve True si los operandos NO se refieren al mismo objeto
aa = 3
bb = 3  
cc = 4
print('AA es BB', aa is bb) # muestra True
print('AA no es BB',aa is not bb) # muestra False
print('AA no es CC', aa is not cc) # muestra True

# Condicionales

# If
edad = 18
if edad < 18:
  print("Menor de edad")
elif edad >= 18:
  print('Mayor de edad')
else:
  print('No se va a ejecutar')


# For
lenguajes = ['Python', 'JavaScript', 'Dart']
for lenguaje in lenguajes:
  print(lenguaje)

# While
contador = 0
while contador < 3:
  print("Dentro del bucle", contador)
  contador += 1



# DIFICULTAD EXTRA

for i in range(10, 56):
  if i % 2 == 0:
    if i != 16 and i % 3 != 0:
      print(i)


"""
### RETO #01 - Operadores y estructuras de control

### 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje

## Operaradores aritméticos
"Se utilizan para realizar operaciones aritméticas"

a, b = 17, 5
print("OPERADORES ARITMÉTICOS\n")
print("Suma de {} + {} = ".format(a,b), (a+b)) # Suma
print("Resta de {} - {} = ".format(a,b), (a-b)) # Resta
print("Multiplicación de {} * {} = ".format(a,b), (a*b)) # Multiplicación
print("División de {} / {} = ".format(a,b), (a/b)) # División
print("Resto entre {} - {} = ".format(a,b), a%b) # Módulo / Resto
print("{} elevado a {} = ".format(a,b), a**b) # Potencia
print("División entera {} + {} = ".format(a,b), a//b) # División entera
print("Valor absoluto de -{}".format(a), abs(-a)) # Absoluto

## Operadores Binarios
"Se usan para realizar operaciones a nivel de bit"

print("\nOPERADORES BINARIOS")
print("\nValor binario de {} y {}, ".format(a,b), bin(a), bin(b))
print("Operador AND: {} & {} = ".format(a,b),a&b) # AND devuelve 1 si ambos coinciden en 1 y el resto de los casos 0. 1AND1=1 / 1AND0, 0AND1, 0AND0 = 0. Fórmula: (a & b) = a x b
print("Operador OR: {} | {} = ".format(a,b),a|b) # OR Retorna 1 si alguno de los bits comparados es 1. 1OR1, 1OR0, 0OR1 = 1, 0OR0 = 0. Fórmula: (a|b) = a + b - (a x b)
print("Operador XOR: {} ^ {} = ".format(a,b),a^b) # XOR (exclusive OR) Devuelve 1 para  1XOR0 o 0XOR1, y 0 para los otros casos. Fórmula: (a^b) = (a+b)mod2
print("Operador NOT: ~{}, ~{} = ".format(a,b),~a,~b) # NOT retorna el valor contrario. Fórmula: ~a = 1 - a 
print("Operador LEFT SHIFT: {} << 1, {} << 1 = ".format(a,b),a<<1,b<<1) # LEFT SHIFT agrega ceros a la izquierda | 0010 << 2 => 1000. Fórmula: a << n = a x 2^n
print(f"Operador RIGTH SHIFT: {a} >> 1, {b} >> 1 = ",a>>1,b>>1) # RIGTH SHIFT agrega ceros a la derecha | 1000 >> 2 => 0010. Fórmula: a >> n = a//2^n


## Operadores de asignación
"Permiten realizar una operación y almacenar su resultado en la variable inicial"

print("\nOPERADORES DE ASIGNACIÓN")
#Suma
a+=b 
print(f"\nAsignación Suma {a} += {b}:", a) 
#Resta
a-=b
print(f"Asignación Resta {a} -= {b}:", a)
#Multiplicación
a*=b
print(f"Asignación Multiplicación {a} *= {b}:", a)
#División
a/=b
print(f"Asignación División {a} /= {b}:", a)
#Módulo
a%=b
print(f"Asignación Módulo {a} %= {b}:", a)
#Potencia
a**=b
print(f"Asignación Potencia {a} **= {b}:", a)
#Floor
a//=b
print(f"Asignación División entera {a} //= {b}:", a)


#AND
a,b = 17,5
a&=b
print(f"\nAsignación AND {a} &= {b}:", a)
#OR
a,b = 17,5
a|=b
print(f"Asignación OR {a} |= {b}:", a)
#XOR
a,b = 17,5
a^=b
print(f"Asignación XOR {a} ^= {b}:", a)
#LSHIFT
a,b = 17,5
a<<=b
print(f"Asignación LShift {a} <<= {b}:", a)
#RSHIFT
a,b = 17,5
a>>=b
print(f"Asignación RShift {a} >>= {b}:", a)



## Operadores de lógicos
"Permiten operar datos booleanos, True o False"

c, d = True, False
print("\nOPERADORES LÓGICOS")
print(f"\nOperador and: {c} and {d}: ", c and d) # Compara ambos valores y devuelve True si ambos son True
print(f"Operador and: {c} or {d}: ", c or d) # Compara ambos valores y devuelve True si alguno de los dos es True
print(f"Operador and: not {c}, not {d}: ", not c, not d) # Devuelve el valor contrario, True si es False, False si es True

## Operadores relacionales
"Permiten comparar entre dos variables, devuelven valores True or False si las condiciones se cumplen"

a,b = 17,5
print("\nOPERADORES RELACIONALES" )
print(f"Operador Igual: {a} == {b}: ", a == b)
print(f"Operador Distinto: {a} != {b}: ", a != b)
print(f"Operador Mayor: {a} > {b}: ", a > b)
print(f"Operador Menor: {a} < {b}: ", a < b)
print(f"Operador Mayor o Igual: {a} >= {b}: ", a >= b)
print(f"Operador Menor o Igual: {a} <= {b}: ", a <= b)

## Operadores de identidad
"Compara la ubicación en la memoria de dos objetos"

a,b,c,d = 10,10,[1,2,3],[1,2,3]
print("\nOPERADORES DE IDENTIDAD")
print("\na = 10\nb = 10\nc = [1,2,3]\nd = [1,2,3]")
print("\na is b: ", a is b) # a y b serán iguales si, id(a) e id(b) lo son. El número 10 almacenado por a y b tiene la misma ubicación en la memoria
print("id(a) :", id(a))
print("id(b) :", id(b))
print("c is not d :", c is not d) # c y d no serán iguales si, id(c) e id(d) no lo son. Las listas creadas para c y d corresponden a objetos diferentes, por lo tanto ocupan distintos espacios en la memoria
print("id(c) :", id(c))
print("id(d) :", id(d))

## Operadores de membresia
"Son operadores que nos permiten saber si un elemento esta contenido en una secuencia. Por ejemplo si un número está contenido en una lista de números, devuelven valores True o False"

print("\nOPERADORES DE MEMBRESÍA")
print("\na in c:", a in c) # Si a está contenido dentro de c entonces devolverá True
print("(4,5) not in c:", (4,5) not in c) # Si a no está contenido dentro de c entonces devolverá True


## Operadores de cadenas
"Permite manejar cadenas de texto"

print("\nOPERADORES DE CADENAS")
print("\nConcatenación: 'Buenos ' + 'Días' = ", "Buenos " + "Días")
print("Multiplicación: 'Doble'*3 ", "Doble"*3)
print("Índice: 'Paralelepípedo[3]' = ", "Paralelepípedo"[3])
print("Slicing/range: 'Paralelepípedo[3:8]' = ", "Paralelepípedo"[3:8])
print("Largo de la cadena: len('Paralelepípedo')", len('Paralelepípedo'))
print("Iteración: for i in 'paralelepipedo' print(i)")
for i in 'paralelepipedo':
    print(i)

### 2. Utilizando las operaciones con operadores que tú quieras, 
### crea ejemplos que representen todos los tipos de estructuras 
### de control que existan en tu lenguaje

## Condicionales

# If - Elif - Else

print(
"""
ESTRUCTURAS DE CONTROL

Condicionales: if, elif, else:

a,b = 12, 34

if a == b:
    print (f"{a} es igual a {b}")
elif a > b:
    print (f"{a} es mayor a {b}")
else:
    print(f"{a} debe ser menor que {b}")
""")

a,b = 12, 34

if a == b:
    print (f"{a} es igual a {b}")
elif a > b:
    print (f"{a} es mayor a {b}")
else:
    print(f"{a} debe ser menor que {b}")

## De Bucle

# For - While - Break - Continue - Pass

"""
i = 0
while i < len("exterior"):
    print (f"\nIteración en {'exterior'[i]}")
    for j in  "interior":
        if j == "n":
            print(f"Continuing el búcle interior en la letra {j}")
            continue # Salta la letra n y continua el búcle
        elif j == "t":
            print(f"Passing el búcle interior en la letra {j}")
            pass # No pasa nada
        elif j == "o":
            print(f"Breaking el búcle interior en la letra {j}")
            break # Sale del búcle en la letra o
    if "exterior"[i] == "r":
        break
    i += 1
print ("\nFin del búcle")    
"""

i = 0
while i < len("exterior"):
    print (f"\nIteración en {'exterior'[i]}")
    for j in  "interior":
        if j == "n":
            print(f"Continuing el búcle interior en la letra {j}")
            continue # Salta la letra n y continua el búcle
        elif j == "t":
            print(f"Passing el búcle interior en la letra {j}")
            pass # No pasa nada
        elif j == "o":
            print(f"Breaking el búcle interior en la letra {j}")
            break # Sale del búcle en la letra o
    if "exterior"[i] == "r":
        break
    i += 1
print ("\nFin del búcle")        

## Excepciones

# Try - except - raise - finally


def excepciones(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        result = None 
    except TypeError:
        print("Error: Tipos de datos deben ser compatibles.")
        result = None
    else:
        print(f"El resultado es {result}")
    finally:
        print("Operación terminada")
    return result

print("\nEXCEPCIONES\n")
print(
    """
def excepciones(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        result = None 
    except TypeError:
        print("Error: Tipos de datos deben ser compatibles.")
        result = None
    else:
        print(f"El resultado es {result}")
    finally:
        print("Operación terminada")
    return result\n\n
"""
)

print (f"Caso 1, a = 10, b = 0")
excepciones(10,0)
print (f"\nCaso 2, a = 10, b = '0'")
excepciones(10,"0")
print (f"\nCaso 3, a = 10, b = 5")
excepciones(10,5)

## EXTRA    
"Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3"

for i in range(10,56):
    if (i%2 == 0) and i != 16 and (i%3!=0):
        print(i)

## versión list comprehesion
## numero = [i for i in range(10,56) if (i%2 == 0) and i != 16 and (i%3!=0)]
## print (numero)
"""
