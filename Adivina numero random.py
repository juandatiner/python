import random
print('Hola')
print('Intenta adivinar el numero')
numero_elegido=random.randint(1,5)
numero_correcto=int(input('Dime un numero del 1 al 5: '))
if numero_correcto != numero_elegido :
    print('Perdiste, Intentalo de nuevo')
if numero_correcto == numero_elegido :
    print('Wow adivinaste!!')
print('El numero ganador era: {}'.format(numero_elegido ))