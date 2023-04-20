numero=12

while numero <100:
    print('Mi numero {} es mayor que 1'.format(numero))
    numero +=1




----------------------------------------------------------------------------------------------

respuesta_correcta = None

while respuesta_correcta != 'A' and respuesta_correcta != 'B' and respuesta_correcta != 'C':
    respuesta_correcta=input('Elije una letra [A,B,C]\n'
              'Rta: ')

if respuesta_correcta == 'A':
    print('Alto')

elif respuesta_correcta == 'B':
    print('Bajo')

elif respuesta_correcta == 'C':
    print('Normal')

else:
    print('No me has dado una respuesta con sentido')
