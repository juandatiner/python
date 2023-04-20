titulo= 'Buenos dias!!'
print(titulo +'\n'+ '_' * len(titulo)+'\n'
      'Te ayudare a encontrar tu nuevo celular')


gusto_usuario=input('¿Prefieres IOS o ANDROID?: ')

if gusto_usuario=='IOS':
    iOS=input('¿Tienes dinero?(SI/NO): ')
    if iOS=='NO':
        print('iPhone de segunda mano')
    elif iOS=='SI':
        print('iPhone Ultra Pro Max')
    else:
        print('Opcion incorrecta')
        exit()

elif gusto_usuario=='ANDROID':
    android=input('¿Tienes dinero?(SI/NO): ')
    if android=='NO':
        print('Huawei o Xiaomi (Gama baja)')
    elif android=='SI':
        print('Samsung Fold 3')
    else:
        print('Opcion incorrecta')
        exit()


else:
    print('Opcion incorrecta')
    exit()

