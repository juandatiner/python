vocales=['a','e','i','o','u']
frase='Hello my friend, my name is Juan DAvid Rincon Muñoz and I live in Bogota, Colombia with my mom and my grand' \
      'parents, my mom is the mom in the world. she is so beautiful and I love her' \
      ' alot, thank yoou for read and give some time while I hacked you, xoxo'
vocales_encontradas=0

for letra in frase:
      if letra in vocales:
            print('He encontrado esta vocal {}'.format(letra))
            vocales_encontradas +=1


print('Vocales encontradas: {}'.format(vocales_encontradas))