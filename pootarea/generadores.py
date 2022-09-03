def generamultiplo7(limite):
    numero = 1
    listanumeros=[]

    while numero <= limite:
        listanumeros.append(numero * 7)
        numero=numero+1
    return listanumeros
print(generamultiplo7(10))


def generadormultiplo7(limite):
    numero=1

    while numero <= limite :
        yield numero *7
        numero=numero+1

obtinenmultplo7=generadormultiplo7(10)

#print(obtinenmultplo7)

for n in obtinenmultplo7:
    print(n)
#next retona el siguinete elemonto

print(next(obtinenmultplo7))
print("aca hay 300lineas de codigo..............")
print(next(obtinenmultplo7))
print("aca hay 1000 lineas de codigo")
print(next(obtinenmultplo7))