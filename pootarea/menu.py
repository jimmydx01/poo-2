import os
from math import factorial

from generadores2 import generadores
#from generadores import generador
from POO.cuenta import Cuenta
from POO.curso import Curso
from POO.herencia import Estudiante
from POO.HERENCIA_MULTIPLE import ClaseX
from POO.persona import Persona
from POO.polimorfismo import Trabajador, describirPersona
from POO.relaciones_clases import Ciudad, Pais, Urbanizacion
from break_continiu_pass import break_continue
from for1 import for_p
from if1 import ifin
from ingresoDatos import ingresodatos
from modulos.modulos import Modulos
from operadorteernario import operador_ternario
from operadorteernario import matematicas
from operadoresloguicos import operadoreslogicos


from cadenas import cadenas
from concatenacion import concatenar1
from diccionarios import diccionarios
from excepciones import exepciones
#from funciones import  funciones
from if_else import ifelse
from paquete1.funcionesnumericas import *
from range0 import range1


class Menu:
    def _init_(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc


opc = ""
while opc != "34":
    os.system("cls")
    men = Menu("Menu Principal",
               ["1)Hola mundo", "2)Listas", "3)Variables", "4)conversiones", "5)Operaciones Aritmeticas",
                "6)concatenar", "7)Cadenas", "8)Tuplas", "9)Diccionario", "10)", "11)", "12)", "13)", "14)", "15)",
                "16)", "17)", "18)", "19)", "20)", "21)", "22)", "23)", "24)", "25)", "26)", "27)", "28)", "29)", "30)",
                "31)", "32)", "33)", "34)salir"])
    opc = men.menu()
    # ________________________________________
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos = (input("Ingrese nombre a imprimir: "))
        if Elementos == "":
            ele = 3
        else:
            ele = Elementos
        resultados = Imprimir(ele)

        # ________________________________________
        while opc1 != "2":
            os.system("cls")
            men1 = Menu("Menu imprimir ", ["1)Mostrar", "2)Salir"])
            opc1 = men1.menu()
            # ________________________________________
            if opc1 == "1":
                os.system("cls")
                print("<---Mostrar--->")
                res = resultados.pr()
                input("Presione una tecla para continuar...")
            # ________________________________________
    if opc == "2":

        opc1 = ""
        os.system("cls")
        resultados = ReLista()
        # ________________________________________
        while opc1 != "9":
            os.system("cls")
            men1 = Menu("Menu Operaciones listas",
                        ["1)Mostrar Lista", "2)Mostrar un elemento de la lista", "3)Agregar elemento a la lista",
                         "4)Ver operacion de listas con posicion", "5)insertar en lista", "6)Indice de lista",
                         "7)Remover lista", "8)Sacar de lista", "9) Salir"])
            opc1 = men1.menu()
            # ________________________________________
            if opc1 == "1":
                os.system("cls")
                print("<---Mostrar--->")
                res = resultados.mostrarLis()
                print(res)
                input("Presione una tecla para continuar...")
            # ________________________________________
            elif opc1 == "2":
                os.system("cls")
                print("<---Mostar Elemento--->")
                res = resultados.mostrarLis()
                print(res)
                num = len(res)
                print("<---De acuerdo a la lista escoja una posicion numero positivo y menor a {}--->".format(num))
                r = int(input("Ingrese Posicion: "))
                if r == 6:
                    print("posicion no encontrada")
                else:
                    res = resultados.Mostrar1(r)
                input("Presione una tecla para continuar...")
            # ________________________________________
            elif opc1 == "3":
                os.system("cls")
                print("<---Agregar Elemento--->")
                opc1 = ""
                while opc1 != "3":
                    os.system("cls")
                    men1 = Menu("Menu de elecion de tipo variable", ["1)numero", "2)texto", "3)Salir"])
                    opc1 = men1.menu()

                    if opc1 == "1":
                        os.system("cls")
                        ele = input("ingrese elemento a agregar: ")
                        res = resultados.agregar(int(ele))
                        input("Presione una tecla para continuar...")

                    elif opc1 == "2":
                        os.system("cls")
                        ele = input("ingrese elemento a agregar: ")
                        res = resultados.agregar(ele)
                        input("Presione una tecla para continuar...")


            # ________________________________________
            elif opc1 == "4":
                os.system("cls")
                print("<---View de listas Distintas maneras de ver elementos de lista--->")
                res = resultados.mostrarLis()
                print(res)
                print("============================================ ")

                resultados.viewlist()
                input("Presione una tecla para continuar...")
            # ________________________________________
            elif opc1 == "5":
                os.system("cls")
                print("<---Insertar en posicion especifica--->")
                pos = int(input("Ingrese Posicion a colocar: "))
                nom = input("ingrese elemento a ingresar: ")
                resultados.insertar(pos, nom)
                print(resultados.mostrarLis())
                input("Presione una tecla para continuar...")

            elif opc1 == "6":
                os.system("cls")
                print("<---Indice de elementos--->")
                print(resultados.indiceElem())
                input("Presione una tecla para continuar...")


            elif opc1 == "7":
                os.system("cls")
                print("<---remover elementos de la lista--->")
                opc1 = ""
                while opc1 != "3":

                    os.system("cls")
                    print(resultados.mostrarLis())
                    men1 = Menu("Que desea remover ", ["1)numero", "2)texto", "3)Salir"])
                    opc1 = men1.menu()

                    if opc1 == "1":
                        os.system("cls")
                        print(resultados.mostrarLis())
                        ele = input("ingrese elemento a remover: ")
                        res = resultados.remover(float(ele))
                        print(resultados.mostrarLis())
                        input("Presione una tecla para continuar...")

                    elif opc1 == "2":
                        os.system("cls")
                        print(resultados.mostrarLis())
                        ele = input("ingrese elemento a remover: ")
                        res = resultados.remover(ele)
                        print(resultados.mostrarLis())
                input("Presione una tecla para continuar...")

            elif opc1 == "8":
                os.system("cls")
                print("<---Sacar elemento de la lista--->")
                resultados.sacar()
                print(resultados.mostrarLis())
                input("Presione una tecla para continuar...")

    # ________________________________________
    if opc == "3":

        opc1 = ""
        os.system("cls")

        # ________________________________________
        while opc1 != "2":
            os.system("cls")
            men1 = Menu("Menu Variables", ["1)ver variables", "2)Salir"])
            opc1 = men1.menu()
            # ________________________________________
            if opc1 == "1":
                os.system("cls")
                print("<---Ver Variables--->")
                ver()
                input("Presione una tecla para continuar...")


    # ________________________________________
    elif opc == "4":
        opc1 = ""
        os.system("cls")
        print("<---Ver Conversiones--->")
        mostrarconversiones()
        input("Presione una tecla para continuar...")


    elif opc == "5":
        opc1 = ""
        os.system("cls")
        print("<---Operaciones matematicas--->")
        matematicas()
        input("Presione una tecla para continuar...")

    elif opc == "6":
        opc1 = ""
        os.system("cls")
        print("<---Concatenar Listas--->")
        concatenar1()
        input("Presione una tecla para continuar...")

    elif opc == "7":
        opc1 = ""
        os.system("cls")
        print("<---Cadenas--->")
        cadenas()
        input("Presione una tecla para continuar...")

    elif opc == "8":
        opc1 = ""
        os.system("cls")
        print("<---Tuplas--->")
        tuplas()
        input("Presione una tecla para continuar...")

    elif opc == "9":
        opc1 = ""
        os.system("cls")
        print("<---Diccionario--->")
        diccionarios()
        input("Presione una tecla para continuar...")

    elif opc == "10":
        opc1 = ""
        os.system("cls")
        print("<---Ingreso de datos--->")
        ingresodatos()
        input("Presione una tecla para continuar...")

    elif opc == "11":
        opc1 = ""
        os.system("cls")
        print("<---If Else--->")
        ifelse()
        input("Presione una tecla para continuar...")

    elif opc == "12":
        opc1 = ""
        os.system("cls")
        print("<---If in--->")
        ifin()
        input("Presione una tecla para continuar...")

    elif opc == "13":
        opc1 = ""
        os.system("cls")
        print("<---Funciones--->")
        funciones()
        input("Presione una tecla para continuar...")

    elif opc == "14":
        opc1 = ""
        os.system("cls")
        print("<---Operadores logicos--->")
        operadoreslogicos()
        input("Presione una tecla para continuar...")

    elif opc == "15":
        opc1 = ""
        os.system("cls")
        print("<---Operador Ternario--->")
        operador_ternario()
        input("Presione una tecla para continuar...")

    elif opc == "16":
        opc1 = ""
        os.system("cls")
        print("<---Funcion Range--->")
        range1()
        input("Presione una tecla para continuar...")

    elif opc == "17":
        opc1 = ""
        os.system("cls")
        print("<---Bucles For--->")
        for_p()
        input("Presione una tecla para continuar...")

    elif opc == "18":
        opc1 = ""
        os.system("cls")
        print("<---Factorial--->")
        factorial()
        input("Presione una tecla para continuar...")
    elif opc == "19":
        opc1 = ""
        os.system("cls")
        print("<---Bucle While--->")
        whilee()
        input("Presione una tecla para continuar...")

    elif opc == "20":
        opc1 = ""
        os.system("cls")
        print("<---Brake_continue_pass--->")
        break_continue()
        input("Presione una tecla para continuar...")

    elif opc == "21":
        opc1 = ""
        os.system("cls")
        print("<---Generadores--->")
        generadores()
        input("Presione una tecla para continuar...")

    elif opc == "22":
        opc1 = ""
        os.system("cls")
        print("<---Generadores2--->")
        generadores2()
        input("Presione una tecla para continuar...")

    elif opc == "23":
        opc1 = ""
        os.system("cls")
        print("<---Exepciones--->")
        exepciones()
        input("Presione una tecla para continuar...")

    elif opc == "24":
        opc1 = ""
        os.system("cls")
        print("<---Raise--->")
        raisepp(17)
        input("Presione una tecla para continuar...")

    elif opc == "25":
        opc1 = ""
        os.system("cls")
        print("<---Modulos--->")
        Modulos()
        input("Presione una tecla para continuar...")

    elif opc == "26":
        opc1 = ""
        os.system("cls")
        print("<---Paquete--->")
        print(multiplicar(5, 6))
        print(contar_letras("Hola"))
        input("Presione una tecla para continuar...")

    elif opc == "27":
        opc1 = ""
        os.system("cls")
        print("<---Persona--->")
        persona1 = Persona()
        persona1.apellidos = "García Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellidos = "Paz Torres"
        print(persona2.apellidos)
        # persona2.despertar()
        print(persona2.despierta)
        input("Presione una tecla para continuar...")

    elif opc == "28":
        opc1 = ""
        os.system("cls")
        print("<---Curso--->")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1)
        curso1.mostrarDatos()
        input("Presione una tecla para continuar...")

    elif opc == "29":
        opc1 = ""
        os.system("cls")
        print("<---Cuenta--->")
        cuenta1 = Cuenta("Oscar García", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dólares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")

    elif opc == "30":
        opc1 = ""
        os.system("cls")
        print("<---Herencia--->")
        estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        input("Presione una tecla para continuar...")

    elif opc == "31":
        opc1 = ""
        os.system("cls")
        print("<---Herencia Multiple--->")
        cX1 = ClaseX(15, 21)
        input("Presione una tecla para continuar...")

    elif opc == "32":
        opc1 = ""
        os.system("cls")
        print("<---Polimorfismo--->")
        doc1 = Trabajador()
        describirPersona(doc1)
        input("Presione una tecla para continuar...")

    elif opc == "33":
        opc1 = ""
        os.system("cls")
        print("<---Relaciones Clases--->")
        pais1 = Pais("Perú", "Martín Vizcarra")
        print(pais1)

        ciudad1 = Ciudad("Chiclayo", 150000, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("María de los Angeles", ciudad1)
        print(urba1)
        input("Presione una tecla para continuar...")

    print("Lo espermos en una proxima ocasión")