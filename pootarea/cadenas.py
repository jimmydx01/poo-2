texto = "bienvenidos a mi tarea "
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())


print(texto.find("a"))#posision en dodende se encutra
print(texto.count("e"))#cantida de ocurencias
textofinal=texto.replace("e","3")
print(textofinal)

valar= texto.isnumeric()
print(valar)

cadenaseparada=texto.split(" ")
print(cadenaseparada)