titulo="Bienvenido al test de las gomitas"
print("\n"+titulo +"\n"+"_"*len(titulo)+"\n")

puntuacion=0

opcion=input("Pregunta 1: ¿Que sabor de gomas te gusta mas?\n"
             "A:Acidas\n"
             "B:Azucaradas\n"
             "C:Simples\n"
             "Rta: ")

if opcion == "A":
    puntuacion +=10
elif opcion == "B":
    puntuacion +=20
elif opcion == "C":
    puntuacion +=0
else:
    print("Las opciones posibles son A, B, C.")
    exit()


opcion=input("Pregunta 2: ¿Que marca de gomitas prefieres?\n"
             "A:Grissly\n"
             "B:Trululu\n"
             "C:Vidal\n"
             "Rta: ")

if opcion =="A":
    puntuacion +=10
elif opcion =="B":
    puntuacion +=20
elif opcion =="C":
    puntuacion +=0
else:
    print("Las opciones posibles son A, B, C.")
    exit()


opcion=input("Pregunta 3:¿Con quien comerias gomitas\n"
             "A:Novi@\n"
             "B:Amig@\n"
             "C:Familiar\n"
             "Rta: ")

if opcion =="A":
    puntuacion +=10
elif opcion == "B":
    puntuacion +=20
elif opcion == "C":
    puntuacion +=0
else:
    print("Las opciones posibles son A, B, C.")
    exit()


if puntuacion >=45:
    print("Felicidades!!! Eres un completo fan de las gomitas. ¿Nos casamos?")
elif puntuacion >=20:
    print("Muy bien, me caes bien ;)")
else:
    print("¿Que pasa pai? Muy suave")