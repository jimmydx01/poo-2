print("----cursos-----")
print("matematicas,biologia,ciencias")
cursos= input("ingrese su curso ")
print(cursos)
if cursos in ("matematicas,biologia,ciencias"):
    print("curso{0} selecionados".format(cursos))
else:
    print("curso no existente.........")

