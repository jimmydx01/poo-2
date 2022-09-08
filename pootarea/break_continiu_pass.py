for numero in range(1,6):
    if numero==3:
        break #descanso o interucion
    print("el numero es: {0}".format(numero))

print("bucle terminado")


#continue: omite un aparte del bul¿cle cuando cumple copn la condicion
for numero in range(1, 6):
    if numero == 3:
        continue
    print("el numero es: {0}".format(numero))

print("bucle terminado")

#pass : permite continuar con una sentecia con funcion que  ya no tiene o aun no tine un bloque de cogigo util

for numero in range(1, 6):
    if numero <= 3:
        pass
    else:
        print("el siguinete valor es mayor a 3 ")

    print("el numero es: {0}".format(numero))

print("bucle terminado")

def funcionsinimplemetar ():
    pass


def break_continue():
    return None