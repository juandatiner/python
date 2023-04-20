
numero1=int(input('Dime un numero: '))
print('ok')
numero2=int(input('Dime otro numero: '))
print('Nada mal ;)')
numero3=int(input('Dime un ultimo numero: '))
print('Ahora te dire cual es el mayor y menor')
print('Entre los numeros {},{} y {}, el mayor es: {}, y el menor es: {}'.format(numero1, numero2,numero3,
                                                                                max(numero1, numero2,numero3),
                                                                                min(numero1, numero2,numero3)))