print('Buenos dias')
print('Ve a la cocina y prepara un colacao')
print('Abré la nevera')

hay_leche= input('¿Hay leche? (S/N)')
hay_colacao=input('¿Hay colacao? (S/N)')

if hay_leche != 'S' or hay_colacao != 'S':
    print('Ve hasta el super')
    if hay_leche != 'S':
        print('Compra leche')
    if hay_colacao != 'S':
        print('Compra colacao')

print('Saca un vaso')
print('Sirve leche')
print('Coloca colacao')
print('Mezcla')