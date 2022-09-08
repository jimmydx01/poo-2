opcion = '0'
while not (opcion == '32'):
    print(' 1. menu HOLA MUNDO 01')
    print(' 2. menu VARIBLES 02')
    print(' 3. menu COVERCIONES 03')
    print(' 4. menu NUMERO OPERACIONES 04')
    print(' 5. menu CONCATENACION 05')
    print(' 6. menu CADENAS 01')
    print(' 7. menu TUPLAS 02')
    print(' 8. menu LISTA 03')
    print(' 9. menu DICCIONARIO 04')
    print(' 10. menu INGRESO DE DATOS 05')
    print(' 11. menu IF_ESLSE 01')
    print(' 12. menu FUNCIONES 02')
    print(' 13. menu OPERADORES LOGUICOS 03')
    print(' 14. menu OPERADORES TERNEARIOS 04')
    print(' 15. menu RANGE 05')
    print(' 16. menu BUCLE FOR 01')
    print(' 17. menu IF CON TUPLAS 02')
    print(' 18. menu FACTORIAL')
    print(' 19. menu WHILE ')
    print(' 20. menu BREAK_CONTINIU')
    print(' 21. menu GENERADORES ')
    print(' 22. menu GENERADORES 2')
    print(' 23. menu EXCECIONES ')
    print(' 24. menu RAISE ')
    print(' 25. menu MODULOS ')
    print(' 26. menu PERSONA ')
    print(' 27. menu POLIMORFISMO')
    print(' 28. menu RELACIONES CLASE')
    print(' 29. menu HERENCIA MULTIPLE')
    print(' 30. menu HERENCIA')
    print(' 31. menu CURSO ')
    print(' 32. menu CUENTA')

    print(' 0. Salir')

    opcion = input('  --- ¿Cuál ejercicio deseas ver ?: ')

    if (opcion == '1'):
        print("Hola mundo")

    elif (opcion == '2'):
        nombre = "jimmy"
        print(nombre)

        edad = 25
        print(edad)

        edad = True
        print(edad)

        sueldo = 205.10
        print(sueldo)

    elif (opcion == '3'):
        numero1 = "35"
        numero2 = "18"
        print(numero1 + numero2)

        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)

        sueldo = 1200.53
        sueldo_entero = int(sueldo)
        print(sueldo_entero)

        valor = "4500.889"
        valordecimal = float(valor)
        print(valordecimal * 3)

        edad = 100
        print(len(str(edad)))

    elif (opcion == '4'):
        entera = 23
        decimal = 31.78
        complejo = 12 + 5j
        booleanos = True

        print(entera)
        print(decimal)
        print(complejo)
        print(booleanos)

        numero1 = 20
        numero2 = 4
        print("SUMA:", (numero1 + numero2))
        print("resta:", (numero1 - numero2))
        print("multiplicacion:", (numero1 * numero2))
        print("divicion:", (numero1 / numero2))
        print("divicion exacta:", (numero1 // numero2))
        print("potencia:", (numero1 ** numero2))


    elif (opcion == '5'):
        texto1 = "hola"
        texto = "mundo"
        textofinal = texto1 + " " + texto
        print(textofinal)
        print("el saludo es: %s %s " % (texto1, texto))
        saludofinal = "saludo {0} {1}".format(texto1, texto)
        print(saludofinal)

        saludofinal12 = "saludo:{x} {y}".format(x=texto1, y=texto)
        print(saludofinal12)

    elif (opcion == '5'):
        texto = "bienvenidos a mi tarea "
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())

        print(texto.find("a"))  # posision en dodende se encutra
        print(texto.count("e"))  # cantida de ocurencias
        textofinal = texto.replace("e", "3")
        print(textofinal)

        valar = texto.isnumeric()
        print(valar)

        cadenaseparada = texto.split(" ")
        print(cadenaseparada)




    elif (opcion == '6'):
        tupla = (1, 2, 3)
        print(tupla)
        tupla2 = (7, "oscar", True, 450.1, 16 + 7j, 15, "felicidad", False)
        print(tupla2)
        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[0:4])
        print(tupla2[-2])
        a, b, c = tupla
        print(a)
        print(b)
        print(c)

        tuplafinal = tupla + tupla3
        print(tuplafinal)

        print(tuplafinal.count(3))

        print(tuplafinal.index(3))

    elif (opcion == '7'):
        lista1 = ["oscar", 25, 98.3, True, "flavio", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("jimmy")
        print(lista1)

        lista1.insert(1, "ecuador")
        print(lista1)

        lista1.extend(["james", 110, False])
        print(lista1)

        print(lista1.index("flavio"))
        lista1.remove(56.3)
        print(lista1)

        lista1.pop()

        print(lista1)

        lista2 = ["milagro", "martinez"]
        lista3 = lista2 + lista1
        print(lista3)

        print(lista2 * 4)
        print("jimmy" in lista1)
    elif (opcion == '8'):
        midiccionario = {"españa": "madrid", "peru": "lima", "alemania": "berlin"}
        print(midiccionario["peru"])
        print(midiccionario)
        midiccionario["venezuela"] = "caracas"
        print(midiccionario)

        midiccionario["españa"] = "barcelona"
        print(midiccionario)

        del midiccionario["españa"]
        print(midiccionario)

        dic2 = {"garcia": "oscar", 25: True, "sueldo": 150.80}
        print(dic2[25])

        llaves = ("españa", "fracia", "inglaterra")
        dicpaises = {llaves[0]: "madrid", llaves[1]: "paris", llaves[2]: "londers"}
        print(dicpaises)

        datospersonales = {"apallidos": "garcia", "anios": {1: 2010, 2: 2011, 3: 2013, 4: 2013, 5: 2014}}
        print(datospersonales)
        print(datospersonales["anios"])

        print(datospersonales.get("ape", "oscar"))
        print(datospersonales.keys())
        valores = list(datospersonales.values())
        print(valores)

    elif (opcion == '9'):
        nombre = input("dime como te llams")
        edad = int(input("ingresa tu edad"))
        sueldo = float(input("ingrese tu suendo"))
        print("hola" + nombre)
        edadfutura = edad + 20
        print("tu edad detro de 20 años sera  :", edadfutura)
        print("tu gans esta catidada : ", sueldo)

    elif (opcion == '10'):
        edad = int(input("dime tu edad"))
        if edad > 18:
            print("eres mayor de edad.")
        elif edad == 18:
            print("tienes solo 18 años ")
        else:
            print("eres menor de edad")


    elif (opcion == '11'):
        def saludar():
            print("jimmy")
            print("martinez")
            print("masacre")
            return "hola"


        print(saludar())


        def evalursueldominimo(sueldo):
            if sueldo >= 450:
                print("cumplees con el sueldo minimo")
            else:
                print("ganas menos que el minimo ")


        evalursueldominimo(100)

    elif (opcion == '12'):
        distancia = 400
        numerohermanos = 3
        salariopadres = 3000
        tienebeneficios = False
        if (distancia > 1000 and numerohermanos > 2) or salariopadres < 2000:
            tienebeneficios = True
        print(not tienebeneficios)
        if (5 > 3) or (8 < 6):
            print("verdad")
        else:
            print("es mentira.... ")




    elif (opcion == '13'):
        sexos = ("hombre", " mujer ")
        posicion = True
        sexo = sexos[posicion]
        print(sexo)
        sexo = sexos[not posicion]
        print(sexo)




    elif (opcion == '14'):
        numero = range(5)
        print(numero[4])
        numero1 = range(4, 10)
        print(numero1[3])
        numero2 = range(10, 100, 8)
        print(numero2[9])


    elif (opcion == '15'):
        for num in range(0, 20, 2):
            print("valor actual:{0}".format(num))
        for i in range(1, 13):
            print("{0}x{1}es :{2}".format(i, i, (i * i)))

            for nom in ["karem", "oscar", "hector", "leonardo"]:
                print("camtidad de letras de {0} es {1} ".format(nom, len(nom)))



    elif (opcion == '16'):
        print("----cursos-----")
        print("matematicas,biologia,ciencias")
        cursos = input("ingrese su curso ")
        print(cursos)
        if cursos in ("matematicas,biologia,ciencias"):
            print("curso{0} selecionados".format(cursos))
        else:
            print("curso no existente.........")




    elif (opcion == '17'):
        numero = int(input("ingrese un numero: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print("el factorial  de {0} es : {1}".format(numero, factorial))








    elif (opcion == '18'):
        while indice < 10:
            print("valor acutal:{0}".format(indice))
            indice = indice + 1

        print("hemos terminado el bucle while")

        inico = 2

        while inico <= 100:
            print("numeor par :{0}".format(inico))
            inico += 2

        print("hemos terminado el bucle while")


    elif (opcion == '19'):
        for numero in range(1, 6):
            if numero == 3:
                break  # descanso o interucion
            print("el numero es: {0}".format(numero))

        print("bucle terminado")

        # continue: omite un aparte del bul¿cle cuando cumple copn la condicion
        for numero in range(1, 6):
            if numero == 3:
                continue
            print("el numero es: {0}".format(numero))

        print("bucle terminado")

        # pass : permite continuar con una sentecia con funcion que  ya no tiene o aun no tine un bloque de cogigo util

        for numero in range(1, 6):
            if numero <= 3:
                pass
            else:
                print("el siguinete valor es mayor a 3 ")

            print("el numero es: {0}".format(numero))

        print("bucle terminado")


        def funcionsinimplemetar():
            pass

    elif (opcion == '20'):

        def generamultiplo7(limite):
            numero = 1
            listanumeros = []

            while numero <= limite:
                listanumeros.append(numero * 7)
                numero = numero + 1
            return listanumeros


        print(generamultiplo7(10))


        def generadormultiplo7(limite):
            numero = 1

            while numero <= limite:
                yield numero * 7
                numero = numero + 1


        obtinenmultplo7 = generadormultiplo7(10)

        # print(obtinenmultplo7)

        for n in obtinenmultplo7:
            print(n)
        # next retona el siguinete elemonto

        print(next(obtinenmultplo7))
        print("aca hay 300lineas de codigo..............")
        print(next(obtinenmultplo7))
        print("aca hay 1000 lineas de codigo")
        print(next(obtinenmultplo7))


    elif (opcion == '21'):

        def devuelbelenguaje(*lenguajes):
            for leng in lenguajes:
                yield from leng


        lengiajes = devuelbelenguaje("python", "java", "ruby", "php")
        print(next(lengiajes))
        print(next(lengiajes))



    elif (opcion == '22'):

        numero = 20
        numero1 = 2

        try:
            resultado = numero / numero1
        except zerodivicionerror:
            print("no se puede dividir entre si")
        finally:
            print("yo siempre aparesco")

        print("aui termina esto")



    elif (opcion == '23'):
        def evaluarnota(nota):
            if nota < 0:
                raise ZeroDivisionError("NO SE PEREMITE VALORES NEGATIVOS.....")
            elif nota >= 16:
                print("exelente")
            elif nota >= 11:
                print("aprobado")
            else:
                print("desaprobado")


        evaluarnota(-1)
        print("este es el fin de mi programa. ")



    elif (opcion == '24'):
        import funcionesmatematicas

        print(funcionesmatematicas.sumar(5, 6))
        print(funcionesmatematicas.multiplicar(5, 6))

    elif (opcion == '25'):

       print("creaciones de paqute ")



    elif (opcion == '26'):
        class Persona():
            # propiedades y carateristicas o atribuotos
            apellidos = " "
            nombre = " "
            edad = 0
            despierta = False

            # funciones
            def despertar(selfs):
                # self es como un parametro que ase referencia a la istacion  o objeto  perteneciente a la clase
                selfs.despierta = True
                print("bunes dias ")


        persona1 = Persona()
        persona1.apellidos = "martinez brito"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellidos = "pastos lopez"
        print(persona2.apellidos)
        # persona2.despertar()
        print(persona2.despierta)




    elif (opcion == '27'):
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


        dpc1 = Trabajador()
        describirpersona(dpc1)


    elif (opcion == '28'):
        class Pais():

            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                txt = "pais:{0}- Presidente:{1}"
                return txt.format(self.nombre, self.presidente)


        class Ciudad():
            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad:{0}-N.- Habitantes : {1}({2})"
                return txt.format(self.nombre, self.habitantes, self.pais)


        class Urbanizacion():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "urbanizacion:{0}({1})"
                return txt.format(self.nombre, self.ciudad)


        pais1 = Pais("Peru", "martin vizcarra")
        print(pais1)

        ciudad1 = Ciudad("lima", 15000, pais1)
        print(ciudad1)

        urb1 = Urbanizacion("maria de los angeles", ciudad1)
        print(urb1)


    elif (opcion == '29'):
        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro = par1
                self.parametro1 = par2


        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro2 = par3
                self.parametro3 = par4
                self.parametro4 = par5


        class ClaseX(ClaseA, ClaseB):
            pass


        cX1 = ClaseX(15, 21)

    elif (opcion == '30'):

        class Persona():
            def __init__(self, apepat, apemat, nom):
                self.apellidopaterno = apepat
                self.apellidosmaterno = apemat
                self.nombres = nom

            def mostrarnombrecompelto(self):
                txt = "{0}{1}{2}"
                return txt.format(self.apellidopaterno, self.apellidosmaterno, self.nombres)

            def datos(self):
                print(self.mostrarnombrecompelto())


        class Estudiante(Persona):
            def __init__(self, apepat, apemat, nom, pro):
                super().__init__(apepat, apemat, nom)
                self.profecion = pro

            def datos(self):
                print("profesion:{0}".format(self.profecion))

            estu1 = Estudiante("Martines ", "brito ", "jimmy ", "DOCTOR")
            print(estu1.mostrarnombrecompelto())
            estu1.datos()
            print(isinstance(estu1, Estudiante))

    elif (opcion == '31'):

        class Curso():
            """
             nombre="matematicas"
            creditos= 5
            profesion ="ingeniereo civil "

            """

            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "presencial"  # propiedad ecansuladad

            def mostradatos(self):
                dat = "nombre: {0}/cerditos{1}/modo de imparticion {2}"
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteasignado = self.__verificardocente()
                if docenteasignado:
                    print("existe docente asignado..")
                else:
                    print("no es nesesario asignar un docente ....")

            def __verificardocente(self):
                print("verificar  si existe el docente asignado..........")
                if self.__imparticion == "presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "Nombre:{0}-cerditos:{1}"
                return texto.format(self.nombre, self.creditos)


        curso1 = Curso("matematicas", 5, "ingieneria civl ")
        print(curso1.nombre)
        curso1.mostradatos()

        curso2 = Curso("lenguaje", 4, "ingieneria sotfware ")
        print(curso2.nombre)
        print(curso1)

    elif (opcion == '32'):

        class Cuenta():
            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            # getters metedos get sir para obtener un valor
            def get_Saldo(self):
                return self.__saldo

            def get_Propietario(self):
                return self.__propietario

            def get_Moneda(self):
                return self.__moneda

            # setters metodos set para modificar un valor
            def set_Moneda(self, moneda):
                self.__moneda = moneda


        cuenta1 = Cuenta("oscar garcia", 15000, "soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("dolares")
        print(cuenta1.get_Moneda())


    elif (opcion == '0'):
        print(' **** Saliendo del menu  ****')
        print(' **** Ejemplo de un menu ****')
    else:
        print('No existe la opcion')







