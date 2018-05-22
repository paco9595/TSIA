def LeerDatos(nombre):
    try :
        archivo = open(nombre,"r")
        suma = ""
        aux = []
        datos = []
        i = 0
        for linea in archivo.readlines():
            for x in linea:
                if x != " " and x != "\n" and x != "-":
                    suma += x
                else:
                    if(len(suma) > 0):
                        aux.append(int(suma))
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return
def leerNombre(nombre):
    try :
        archivo = open(nombre,"r")
        suma = ""
        aux = ""
        datos = []
        i = 0
        for linea in archivo.readlines():
            for x in linea:
                if x != " " and x != "\n" and x != "-":
                    suma += x
                else:
                    if(len(suma) > 0):
                        aux = suma
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return

def buscarPrimero(datos, visitadas, pos):
    print(datos,visitadas, pos + 1)
    for i, x in enumerate(datos):
        if x > 0 and visitadas[i] == 0:
            return i
    return -1
def busqueda_profunda(datos,inicio,fin):
    visitadas = [0] * len(datos)
    visitadas[inicio] = 1
    camino = [inicio]
    posicion = inicio
    costo = 0
    sal1 = False
    iteraciones = 0
    iteraciones1 = 0
    while True and iteraciones < 100000:
        if posicion == fin:
            print('costo', costo)
            return camino
        while not sal1 and iteraciones1 < 100000:
            pos1 = posicion + 0 
            posicion = buscarPrimero(datos[posicion], visitadas, posicion)
            if posicion != -1:
                costo += datos[int(pos1)][posicion]
                visitadas[posicion] = 1
                camino.append(posicion)
                sal1 = True
            else:
                eliminar = camino.pop()
                costo -= datos[int(pos1)][eliminar]
                posicion = camino[ len(camino) - 1]
            iteraciones1 += 1
        sal1 = False
        iteraciones1 = 0
        iteraciones += 1
    print('fatal Error')
    return []

def Main():
    ciudades = leerNombre('../Txt/nombres_alemania.txt')
    datos = LeerDatos('../Txt/alemania.txt')
    visitadas = [0] * len(datos)
    final = busqueda_profunda(datos,0,13)
    print('caminio',final)
    for x in final:
        print(x + 1,("-.")if x + 1 >= 10 else (" -."),ciudades[x])
Main()
