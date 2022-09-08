class Persona():
    #propiedades y carateristicas o atribuotos
    apellidos=" "
    nombre=" "
    edad=0
    despierta=False

    #funciones
    def despertar(selfs):
        #self es como un parametro que ase referencia a la istacion  o objeto  perteneciente a la clase
        selfs.despierta=True
        print("bunes dias ")

persona1=Persona()
persona1.apellidos="martinez brito"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2=Persona()
persona2.apellidos="pastos lopez"
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)