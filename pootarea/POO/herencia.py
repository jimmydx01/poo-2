class Persona():
    def __init__(self,apepat,apemat,nom):
        self.apellidopaterno=apepat
        self.apellidosmaterno=apemat
        self.nombres=nom
    def mostrarnombrecompelto(self):
        txt="{0}{1}{2}"
        return txt.format(self.apellidopaterno,self.apellidosmaterno,self.nombres)

    def datos(self):
        print(self.mostrarnombrecompelto())

class Estudiante(Persona):
    def __init__(self,apepat,apemat,nom,pro):
        super().__init__(apepat,apemat,nom)
        self.profecion=pro
    def datos(self):
        print("profesion:{0}".format(self.profecion))


estu1=Estudiante("Martines ", "brito ", "jimmy ","DOCTOR")
print(estu1.mostrarnombrecompelto())
estu1.datos()
print(isinstance(estu1,Estudiante))






