print('Buenos dias, Bienvenido a Convensor de divisas')
'\n'
dolar_euro= 0.85
dolar_pesocolombiano=3.836
euro_pesocolombiano=4.487

opcion=input('¿Que divisa quieres convertir?\n'
             'A - dolar a euro\n'
             'B - dolar a peso colombiano\n'
             'C - euro a peso colombiano \n'
             'D - euro a dolar\n'
             'E - peso colombiano a dolar\n'
             'F - peso colombiano a euro\n'
             'Rta: ')

texto_usuario= 'Introduzca la cantidad de {} a convertir: '

if opcion == 'A':
    cantidad_divisas = float(input(texto_usuario.format('dolares')))
    print('La cantidad en euros es: {}'.format(cantidad_divisas*dolar_euro))

elif opcion == 'B':
    cantidad_divisas = float(input(texto_usuario.format('dolares')))
    print('La cantidad en pesos colombianos es: {}'.format(cantidad_divisas*dolar_pesocolombiano))

elif opcion == 'C':
    cantidad_divisas = float(input(texto_usuario.format('euros')))
    print('La cantidad en pesos colombianos es: {}'.format(cantidad_divisas*euro_pesocolombiano))

elif opcion == 'D':
    cantidad_divisas = float(input(texto_usuario.format('euros')))
    print('La cantidad en dolares es: {}'.format(cantidad_divisas/dolar_euro))

elif opcion == 'E':
    cantidad_divisas = float(input(texto_usuario.format('pesos colombianos')))
    print('La cantidad en dolares es: {}'.format(cantidad_divisas/dolar_pesocolombiano))

elif opcion == 'F':
    cantidad_divisas = float(input(texto_usuario.format('pesos colombianos')))
    print('La cantidad en euros es: {}'.format(cantidad_divisas/euro_pesocolombiano))

else:
    print('Respuesta erronea, intentalo nuevamente.')
    exit()