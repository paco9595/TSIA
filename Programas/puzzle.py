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
                        aux.append(float(suma))
                        suma = ""
            if(len(aux)>0):
                i += 1
                datos.append(aux)
                aux = []
        return datos
    except ValueError:
        print('format error')
        return 

def menu(opciones, texto):
    opcion = -100
    while(opcion < 0 or opcion > len(opciones)):
        while True:
            print('\t Menu Selecione una opcion')    
            print(texto)
            for i, x in enumerate(opciones):
                print(str(i+1)+ "-. "+ str(x))
            try:
                opcion = int(input("ingrese una opcion valida: "))
                break
            except ValueError:
                os.system ("cls")
                print("ingrese una opcion valida")
    return opcion

def GenerarRandom():
    pass
def Manual():
    pass
def printMatrix(datos):
    for x in range(len(datos)):
        print(datos[x])
def sacarDiferencias(datos):
    diferencias = [[1,2,3],[4,5,6],[7,8,0]]
    suma = 0
    for i, x in enumerate(datos):
        for y, z in enumerate(datos[i]):
            diferencias[i][y] = (z - diferencias[i][y])
            if diferencias[i][y] < 0:
                diferencias[i][y] *= -1
                suma += diferencias[i][y]
            else:
                suma += diferencias[i][y]
    print(suma)
    return diferencias
def Main():
    opcion = menu(["archivo de texto","Random","Manual"], 'leer datos por medio de: ')
    datos = {
        1: LeerDatos('../txt/puzzle.txt'),
        2: GenerarRandom(),
        3: Manual()
    }.get(opcion,2)
    if(not(datos)):
        return
    print(datos)
    printMatrix(datos)
    sacarDiferencias(datos)
    
Main()