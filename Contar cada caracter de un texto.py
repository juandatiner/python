import string
texto_usuario=input('Introduce un texto: ')
espacios=0
comas=0
puntos=0
letras_mayusculas=0
letras_minusculas=0


for letra in texto_usuario:
	if letra==' ':
		espacios +=1
	elif letra==',':
		comas +=1
	elif letra=='.':
		puntos +=1
	elif letra in string.ascii_uppercase:
		letras_mayusculas +=1
	elif letra in string.ascii_lowercase:
		letras_minusculas +=1

print('\nLo que escribiste tiene:\n'
	  'Espacios: {}\n'
	  'Comas: {}\n'
	  'Puntos: {}\n'
	  'Letras Mayusculas: {}\n'
	  'Letras Minisculas: {}'
	  .format(espacios,comas,puntos,letras_mayusculas,letras_minusculas))