def  evaluarnota(nota):
    if nota < 0:
       raise ZeroDivisionError("NO SE PEREMITE VALORES NEGATIVOS.....")
    elif nota >=16:
        print("exelente")
    elif nota >=11:
         print("aprobado")
    else:
        print("desaprobado")
evaluarnota(-1)
print("este es el fin de mi programa. ")
