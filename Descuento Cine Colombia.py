print('Bienvenido a Cinecolombia')
quiero_descuento=input('¿Quiere saber si tiene un descuento en sus entradas? (SI/NO): ')

if quiero_descuento =='SI':
    print('Muy bien')
    edad =int(input('Digame su edad: '))
    tipo_de_carnet=input('Digame su tipo de carnet. E=Estudiante, T=Trabajador, P=Pensionado, N=Ninguno: ')
    if (10 >= edad and tipo_de_carnet =='E') or \
            (16<= edad <=24 and tipo_de_carnet =='E') or \
            (18<= edad <65 and tipo_de_carnet =='T') or \
            (65<= edad and tipo_de_carnet =='P'):
        print('Tiene descuento.')
    else:
        print('No tiene descuento.')

if quiero_descuento =='NO':
    print('Pagara el valor completo')