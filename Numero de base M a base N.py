
def bienvenida():
    print("¿QUIERES CONOCER TU EDAD EN CUALQUIER BASE NUMÉRICA?\n"
    "\nEn este programa podrás conocer la conversión de un número en cualquier base que desees")

def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {

        "f" : 15,
        "e" : 14,
        "d" : 13,
        "c" : 12,
        "b" : 11,
        "a" : 10,

    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)

def obtener_caracter_hexadecimal(valor):

    valor = str(valor)
    equivalencias = {

        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",

    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:

        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)

    return hexadecimal

def hexadecimal_a_decimal(hexadecimal):
    hexadecimal = hexadecimal.lower()

    hexadecimal = hexadecimal[::-1]

    decimal = 0
    posicion = 0
    for digito in hexadecimal:

        valor = obtener_valor_real(digito)
        elevado = 16 **posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion +=1

    return decimal

def decimal_a_base_x(numero, base):

    if numero <= 0:
        return "0"

    resultado = ""

    while numero > 0:

        residuo = int(numero % base)
        numero = int(numero / base)
        resultado = str(residuo) + resultado

    return resultado

def base_x_a_decimal(numero, base):

    decimal = 0
    posicion = 0

    numero = numero[::-1]
    for digito in numero:

        valor_entero = int(digito)
        numero_elevado = int(base ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1

    return decimal



numero_convertido = 0
numero_decimal = 0
numero_binario = 0

valor_ascci = " "


numero = input("Ingrese un número para convertir: ")

base_original = int(input("Ingrese la base: "))

base_a_pasar = int(input("Ingrese la base en la que desea el numero: "))


if base_original == 16:
    
    numero_decimal = hexadecimal_a_decimal(numero)

    numero_convertido = decimal_a_base_x(numero_decimal, base_a_pasar)

else:

    if base_a_pasar == 16:

        numero_decimal = base_x_a_decimal(numero, base_original)

        numero_convertido = decimal_a_hexadecimal(numero_decimal)

    else:

        numero_decimal = base_x_a_decimal(numero, base_original)

        numero_convertido = decimal_a_base_x(numero_decimal, base_a_pasar)


numero_binario = decimal_a_base_x(numero_decimal, 2)



print(str(numero) + ' con base ' + str(base_original) + ' = ' + str(numero_convertido) + ' con base ' + str(base_a_pasar))
print("Numero Decimal = " + str(numero_decimal))
print("Numero Binario = " + str(numero_binario))
print("ASCII = " + chr(numero_decimal))

# print("ASCCI = " + (str(numero_decimal)))
