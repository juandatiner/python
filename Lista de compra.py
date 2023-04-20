cosa=None
lista=[]

print('Bienvenido a mercar.co')

while True:
    cosa=input('¿Que desea comprar? (Q para salir): ')

    if cosa == 'Q':
        break
    elif cosa in lista:
        print('{} ya esta en la lista de compra.'.format(cosa))
        pass
    elif cosa not in lista:
        while True:
            item=input('¿Seguro que quiere añadir {} a la lista de compra? (S/N): '.format(cosa))
            if item =='S':
                print('{} se añadio a la lista'.format(cosa))
                lista.append(cosa)
                break
            elif item =='N':
                print('{} no se añadio a lista'.format(cosa))
                break
            elif item!='S'and item !='N':
                print('Respuesta incorrecta')


if len(lista)<1:
    print('Su lista esta vacia')
else:
    print('La lista de la compra es:')
    print(lista)