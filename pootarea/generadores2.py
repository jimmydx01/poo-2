

def devuelbelenguaje(*lenguajes):
    for leng in lenguajes:
        yield  from  leng


lengiajes=devuelbelenguaje("python","java","ruby","php")
print(next(lengiajes))
print(next(lengiajes))