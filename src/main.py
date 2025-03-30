from personaje import Personaje

Personaje1=Personaje(
    "Jule la destructora",
    6,
    21,
    50,
    19
)
Personaje2=Personaje(
    "Paco el mago",
    50,
    20,
    35,
    16
)

print("\n-----Estado-----\n")
Personaje1.mostrar_estado()
print("Mi ataque premium es un Dragón\n")
print("---------------------------")
Personaje2.mostrar_estado()
print("Mi ataque sorpresa es una pósima toxica\n")

print("\n-----Ataque personaje 1-----\n")
Personaje1.atacar(Personaje2)
print("---------------------------")
Personaje2.recibir_daño(Personaje1.fuerza)
if not Personaje2.estoy_vivo():
    Personaje2.morir()
    exit()

print("\n-----Como venimos?-----\n")
print("Personaje principal: ", Personaje1.nombre)
Personaje1.estoy_vivo()
print("---------------------------")
print("Personaje secundario: ", Personaje2.nombre)
Personaje2.estoy_vivo()

print("\n-----Ataque personaje 2-----\n")
Personaje2.atacar(Personaje1)
print("---------------------------")
Personaje1.recibir_daño(Personaje2.fuerza)

if not Personaje1.estoy_vivo():
    Personaje1.morir()
    exit()

print("\n-----Ya tenemos algun ganador?-----\n")
print("Personaje principal: ", Personaje1.nombre)
Personaje1.estoy_vivo()
print("---------------------------")
print("Personaje secundario: ", Personaje2.nombre)
Personaje2.estoy_vivo()

