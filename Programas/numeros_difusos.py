import os
def LeerDatos(nombre):
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
    return [2345678]

def Manual():
    return [876543]
def Negativo(datos):
    for i in range(len(datos)):
        datos[i] = round(datos[i]-1,2)
        if datos[i] < 0:
            datos[i] *= -1
    print(datos)
def Comparar(datos):
    pass

def Main():
    opcion = menu(["archivo de texto","Random","Manual"], 'leer datos por medio de: ')
    datos = {
        1: LeerDatos('../txt/numeros_difusos.txt'),
        2: GenerarRandom(),
        3: Manual()
    }.get(opcion,2)
    print(datos)
    Negativo(datos[0])
    
     


Main()