resultado=int(0)

texto_usuario=int(input('Hola!!!\n'
                    'Estoy aca para ayudarte con tus operaciones, dime el primer numero: '))
while True:
        signo=input('¿Quieres sumar[+], restar[-], multiplicar[*] o dividir[/]?: ')
        if signo == '+' or signo == '-' or signo == '*' or signo == '/':
            break


texto_usuario_2=int(input('Ahora dime el otro numero: '))

xd='El resultado es:'

if signo=='+':
    print(xd),print(texto_usuario+texto_usuario_2)
elif signo=='-':
    print(xd),print(texto_usuario-texto_usuario_2)
elif signo=='*':
    print(xd),print(texto_usuario*texto_usuario_2)
elif signo=='/':
    print(xd),print(texto_usuario/texto_usuario_2)
