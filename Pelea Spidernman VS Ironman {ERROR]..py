from random import randint
import os

VIDA_INICIAL_IRONMAN=50
VIDA_INICIAL_SPIDERMAN=50
BARRA_VIDA=20

#Pelea_Ironman_vs_Spiderman
vida_ironman=VIDA_INICIAL_IRONMAN
vida_spiderman=VIDA_INICIAL_SPIDERMAN


while vida_ironman>0 and vida_spiderman>0:
    #Se_siguen_enviando_ataques

    #Turno_de_ironman
    print('Turno de Ironman')
    ataque_ironman=randint(1, 4)
    if ataque_ironman== 1:
        #Rayo_Laser
        print('Ironman ataca con rayo laser')
        vida_spiderman-=8
    elif ataque_ironman== 2:
        #Cohetes
        print('Ironman ataca con cohetes')
        vida_spiderman-=9
    elif ataque_ironman== 3:
        # Super_puño
        print('Ironman ataca con Super Puño')
        vida_spiderman -= 5
    else:
        #Nada
        print('Ironman no ataca')


    if vida_spiderman <0:
        vida_spiderman = 0

    if vida_ironman <0:
        vida_ironman = 0

    #Se_muestra_la_vida_restante
    barra_de_vida_spiderman= int(vida_spiderman * BARRA_VIDA /  VIDA_INICIAL_SPIDERMAN)
    print('La vida de Spiderman es:  [{}{}] ({}/{})'.format('*'* barra_de_vida_spiderman, ' ' * (BARRA_VIDA-barra_de_vida_spiderman),
                                                    vida_spiderman, VIDA_INICIAL_SPIDERMAN))

    barra_de_vida_ironman= int(vida_ironman * BARRA_VIDA / VIDA_INICIAL_IRONMAN)
    print('La vida de Ironman es:    [{}{}] ({}/{})'.format('*'* barra_de_vida_ironman, ' ' * (BARRA_VIDA-barra_de_vida_ironman),
                                                  vida_ironman, VIDA_INICIAL_IRONMAN))
    input('Enter para seguir con la pelea\n')

    os.system('cls')


    #Turno_de_Spiderman
    print('Turno de Spiderman')
    ataque_spiderman=None
    while ataque_spiderman!= 'P' and ataque_spiderman!= 'T' and ataque_spiderman!='C' and ataque_spiderman!='N':
        ataque_spiderman=input('Elije tu ataque. P=Puño Aracnido- T=Telaraña Explosiva- C=Cabezazo Literal- N=Nada\n'
                               'Rta:')

    if ataque_spiderman== 'P':
        #Puño_aracnido
        print('Spiderman ataca con Puño Aracnido')
        vida_ironman-=8
    elif ataque_spiderman== 'T':
        #Teleraña_explosiva
        print('Spiderman ataca con Telaraña explosiva')
        vida_ironman-=9
    elif ataque_spiderman== 'C':
        # Cabezazo_literal
        print('Spiderman ataca con Cabezazo literal')
        vida_ironman -= 5
    else:
        #Nada
        print('Spiderman no ataca')


    if vida_ironman <0:
        vida_ironman = 0
    if vida_spiderman <0:
        vida_spiderman = 0


    #Se_muestra_la_vida_restante
    barra_de_vida_ironman= int(vida_ironman * BARRA_VIDA / VIDA_INICIAL_IRONMAN)
    print('La vida de Ironman es:    [{}{}] ({}/{})'.format('*'* barra_de_vida_ironman, ' ' * (BARRA_VIDA-barra_de_vida_ironman),
                                                  vida_ironman, VIDA_INICIAL_IRONMAN))

    barra_de_vida_spiderman = int(vida_spiderman * BARRA_VIDA / VIDA_INICIAL_SPIDERMAN)
    print('La vida de Spiderman es:  [{}{}] ({}/{})'.format('*' * barra_de_vida_spiderman, ' ' * (BARRA_VIDA - barra_de_vida_spiderman),
                                                    vida_spiderman, VIDA_INICIAL_SPIDERMAN))

    input('Enter para seguir con la pelea\n')

    os.system('cls')

if vida_spiderman <= 0:
    print('Ironman gana!!')

if vida_ironman<= 0:
    print('Spiderman gana!!')