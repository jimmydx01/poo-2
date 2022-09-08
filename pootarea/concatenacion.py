texto1="hola"
texto="mundo"
textofinal=texto1+" "+texto
print(textofinal)
print("el saludo es: %s %s " % (texto1,texto))
saludofinal= "saludo {0} {1}".format(texto1,texto)
print(saludofinal)

saludofinal12="saludo:{x} {y}".format(x=texto1,y=texto)
print(saludofinal12)


def concatenar1():
    return None