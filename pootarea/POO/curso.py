class Curso():
    """
     nombre="matematicas"
    creditos= 5
    profesion ="ingeniereo civil "

    """



    def __init__(self , nom, cre, pro ):
        self.nombre=nom
        self.creditos=cre
        self.profesion=pro
        self.__imparticion="presencial"#propiedad ecansuladad


    def mostradatos(self):
        dat="nombre: {0}/cerditos{1}/modo de imparticion {2}"
        print(dat.format(self.nombre,self.creditos,self.__imparticion))
        docenteasignado=self.__verificardocente()
        if docenteasignado:
            print("existe docente asignado..")
        else:
             print("no es nesesario asignar un docente ....")

    def __verificardocente(self):
        print("verificar  si existe el docente asignado..........")
        if self.__imparticion=="presencial":
            return True
        else:
            return False
        
    def __str__(self):
        texto="Nombre:{0}-cerditos:{1}"
        return texto.format(self.nombre,self.creditos)


curso1=Curso("matematicas",5,"ingieneria civl ")
print(curso1.nombre)
curso1.mostradatos()



curso2=Curso("lenguaje",4,"ingieneria sotfware ")
print(curso2.nombre)
print(curso1)