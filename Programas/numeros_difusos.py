import os
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
    return [2345678]

def Manual():
    return [876543]
def Negativo(datos):
    for i in range(len(datos)):
        datos[i] = round(datos[i]-1,2)
        if datos[i] < 0:
            datos[i] *= -1
    return datos
def laU(derecha, izquierda, datos):
    newArray = []
    for i, x in enumerate(derecha):
        if x >= izquierda[i]:
            newArray.append(x)
        else:
            newArray.append(izquierda[i])
    return newArray
def laN(derecha,izquierda, datos):
    newArray = []
    for i, x in enumerate(derecha):
        if x <= izquierda[i]:
            newArray.append(x)
        else:
            newArray.append(izquierda[i])
    return newArray
def Comparar(ex, datos):
    try:
        if(not(type(ex[0]) is list)):
            if int(ex[0]) < 0:
                derecha = Negativo(datos[int(ex[0])*-1])
            else:
                derecha = datos[int(ex[0])]
        else:
            derecha = ex[0]
        if int(ex[2]) < 0:
            izquierda = Negativo(datos[ int(ex[2])*-1 ])
        else:
            izquierda = datos[int(ex[2])]
        operador = ex[1]
    except IndexError:
        print('exprecion invalida 83')
        return
    except ValueError:

        print('exprecion invalida 86')
        return 
    if operador == 'U':
        resultado = laU(derecha,izquierda, datos)
    elif operador == 'N':
        resultado = laN(derecha,izquierda, datos)
    return resultado
def sacarParentesis(ex):
    inicio = ex.find('(')
    fin = ex.rfind(')') 
    if inicio == -1 or fin == -1:
        return []
        
    e = ex[ ex.find('(') + 1 : ex.rfind(')')]
    return e
def ValidarExprecion(ex,datos):
    resultado = []
    e = sacarParentesis(ex)
    if len(e) < 1:
        return
    e = e.split(' ') 
    return solveString(e,datos) 

def solveString(ex,datos):
    resultado = []
    for i, letra in enumerate(ex):
        if len(letra) > 1 and letra[0] !='-':
            print('exprecion invalida 69')
            return
        if letra == 'U' or letra == 'N':
            if i == 0 or i == len(ex) - 1:
                print('exprecion invalida 73')
                return
            if(len(resultado) == 0):
                resultado = Comparar([ex[i-1], letra, ex[i+1]], datos)
            else:
                resultado = Comparar([resultado, letra, ex[i+1]], datos)
    return resultado
def Main():
    opcion = menu(["archivo de texto","Random","Manual"], 'leer datos por medio de: ')
    datos = {
        1: LeerDatos('../txt/numeros_difusos.txt'),
        2: GenerarRandom(),
        3: Manual()
    }.get(opcion,2)
    if(not(datos)):
        return
    print(ValidarExprecion("(1 U -2)",datos),"final")
     


Main()