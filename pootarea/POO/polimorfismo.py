class Estudiante():

    def descibir(self):
        print("soy un buen estudiante")

class Docente():

    def describir(self):
        print("me dedico a enseñar cursos")

class Trabajador():

    def decribir(self):
        print("trabajp dentro de un empresa")

def describirpersona(persona):
    persona.decribir()

dpc1=Trabajador()
describirpersona(dpc1)



