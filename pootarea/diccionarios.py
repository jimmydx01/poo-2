#son estruturras de datos que nos perminten almacenar valores
midiccionario={"españa":"madrid","peru":"lima","alemania":"berlin"}
print(midiccionario["peru"])
print(midiccionario)
midiccionario["venezuela"]="caracas"
print(midiccionario)

midiccionario["españa"]="barcelona"
print(midiccionario)

del  midiccionario ["españa"]
print(midiccionario)

dic2={"garcia":"oscar",25:True,"sueldo":150.80}
print(dic2[25])

llaves=("españa","fracia","inglaterra")
dicpaises={llaves[0]:"madrid",llaves[1]:"paris",llaves[2]:"londers"}
print(dicpaises)

datospersonales={"apallidos":"garcia","anios":{1:2010,2:2011,3:2013,4:2013,5:2014}}
print(datospersonales)
print(datospersonales["anios"])

print(datospersonales.get("ape","oscar"))
print(datospersonales.keys())
valores=list(datospersonales.values())
print(valores)

