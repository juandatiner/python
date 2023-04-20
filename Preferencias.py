import random
titulo='Bienvenidos a Preferencias\n' \
       'Es un juego donde sabras que prefieres para ser feliz.'
print(titulo + '\n'+'__________________'+'\n')

print('1. Te dan la posibilidad de ser feliz, ¿Qué prefieres?\n'
      'a) Conocer y estar con el amor de tu vida\n'
      'b) Viajar al rededor del mundo y conocer todo lo que quieras\n')

print('¿Amor o aventura?')
primera_pregunta=input('ELije muy bien y contesta a o b\n'
                       'Rta: ')

print('----------------'+'\n')

x = random.randint(1, 10)

if primera_pregunta =='a':
    print('Que buena eleccion, el amor. Ahora,¿Como preferirias conocerl@?\n'
          'a) En un Iglesia\n'
          'b) En una fiesta\n')


    segunda_pregunta=input('Elije muy bien y contesta a o b\n'
                           'Rta: ')

    print('----------------' + '\n')

    if segunda_pregunta =='a':
        print('Te gusta mas la tranquilidad. Pero antes de hablarle a esta persona y ser feliz, la vida te pondra un reto muy sencillo')

        prueba=input('¿Quieres hacerlo? (si/no)\n'
                     'Rta: ')

        print('----------------' + '\n')

        if prueba =='si':
            resultado=int(input('Muy bien. Tendras que resolver esta multiplicacion {}*{}'.format(x,x)+'\n' 
                                                                                                    'Rta: '))
            if resultado ==x*x:
                print('Excelente. Espero seas muy feliz con el amor de tu vida.')

            elif resultado !=x*x:
                print('Primero estudia y luego piensa en amor;)\n'
                      'Fin del juego')

        elif prueba =='no':
            print('Debes aprender que en la vida nada es gratis,\n'
                  'Fin del juego.')

        else:
            print('Respuesta incorrecta')
            exit()


    elif segunda_pregunta =='b':
        print('Eres una persona de ambiente. Pero antes de hablarle a esta persona y ser feliz, la vida te pondra un reto muy sencillo')

        prueba2= input('¿Quieres hacerlo? (si/no)\n'
                       'Rta: ')

        print('----------------' + '\n')

        if prueba2 =='si':
            resultado=int(input('Muy bien. Tendras que resolver esta multiplicacion {}*{}'.format(x,x)+'\n' 
                                                                                                    'Rta: '))
            if resultado ==x*x:
                print('Excelente. Espero seas muy feliz con el amor de tu vida.')

            elif resultado !=x*x:
                print('Primero estudia y luego piensa en amor;)\n'
                      'Fin del juego')

        elif prueba2 =='no':
            print('Debes aprender que en la vida nada es gratis,\n'
                  'Fin del juego.')

        else:
            print('Respuesta incorrecta')
            exit()

    else:
        print('Respuesta incorrecta')
        exit()




elif primera_pregunta =='b':
    print('Eres una persona aventurera por lo que veo. Ahora, ¿Prefieres viajar..?\n'
          'a) Solo \n'
          'b) Acompañado\n')

    segunda_preguntab= input('Elije muy bien y contesta a o b\n'
                             'Rta: ')

    print('----------------' + '\n')


    if segunda_preguntab=='a':
        print('La soledad nos ayuda a conocernos a la perfeccion, pero antes de aventurarte a disfrutar de esta travesia, la vida te pondra un reto muy sencillo')

        prueba3= input('¿Quieres hacerlo? (si/no)\n'
                       'Rta: ')

        print('----------------' + '\n')

        if prueba3 == 'si':
            resultado = int(input('Muy bien. Tendras que resolver esta multiplicacion {}*{}'.format(x, x) + '\n'
                                                                                                            'Rta: '))
            if resultado == x * x:
                print('Excelente. Espero seas muy feliz con el amor de tu vida.')

            elif resultado != x * x:
                print('Primero estudia y luego piensa en amor;)\n'
                      'Fin del juego')

        elif prueba3 == 'no':
            print('Debes aprender que en la vida nada es gratis,\n'
                  'Fin del juego.')

        else:
            print('Respuesta incorrecta')
            exit()

    elif segunda_preguntab=='b':
        print('Si sabemos elejir una buena compañia, sera la mejor experiencia, apoyo y risas no te haran falta, pero antes la vida te pondra un reto muy sencillo')

        prueba4= input('¿Quieres hacerlo? (si/no)\n'
                       'Rta: ')

        print('----------------' + '\n')

        if prueba4 == 'si':
            resultado = int(input('Muy bien. Tendras que resolver esta multiplicacion {}*{}'.format(x, x) + '\n'
                                                                                                            'Rta: '))
            if resultado == x * x:
                print('Excelente. Espero seas muy feliz con el amor de tu vida.')

            elif resultado != x * x:
                print('Primero estudia y luego piensa en amor;)\n'
                      'Fin del juego')

        elif prueba4 == 'no':
            print('Debes aprender que en la vida nada es gratis,\n'
                  'Fin del juego.')

        else:
            print('Respuesta incorrecta')
            exit()
    else:
        print('Respuesta incorrecta')
        exit()

else:
    print('Respuesta incorrecta')
    exit()
