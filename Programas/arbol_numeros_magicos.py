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
def sacarRestas(datos,final):
    aux = []
    resultado = []
    for i, x in enumerate(datos):
        for j, y in enumerate(x):
            aux.append(abs(y-final[i][j]))
        resultado.append(aux)
        aux = []
    return resultado
def sacarMovimentos(datos):
    posible = []
    for i, x in enumerate(datos):
        if x.count(0) > 0:
            posX = i
            posY = x.index(0)
    if posX > 0:
        posible.append([posX - 1, posY])
    if posX < len(datos)-1:
        posible.append([posX + 1, posY])
    if posY > 0:
        posible.append([posX, posY - 1])        
    if posY < len(datos[0]) -1:
        posible.append([posX, posY + 1])
    return posible
def mover(datos,pos):
    alterno = [i[:] for i in datos]
    for i, x in enumerate(alterno):
        if x.count(0) > 0:
            posX = i
            posY = x.index(0)
    aux = alterno[posX][posY]
    alterno[posX][posY] = alterno[pos[0]][pos[1]]
    alterno[pos[0]][pos[1]] = aux
    return alterno
def sumar(datos):
    resultado = 0
    for x in datos:
        resultado += sum(x)
    return resultado
def eleminarMayores(datos):
    menor = min(datos)
    resultado = []
    for i, x in enumerate(datos):
        if x == menor:
            resultado.append()
    return resultado
def hacerMovimento(espacio,visitados,final):
    sumas = []
    aux = 0
    iteracioens = 0
    diferencias = []
    while True and iteracioens < len(espacio):
        for x in espacio:
            aux = sacarRestas(x,final)
            diferencias.append(aux)
            sumas.append(sumar(aux))
        pos = sumas.index(min(sumas))
        print(len(espacio))
        if espacio[pos] in visitados:
            sumas[pos] = max(sumas) + 1
            iteracioens += 1
        else:
            print('hola', espacio[pos])
            return espacio[pos]
        sumas = []
    return -1
def algoritmo(datos):
    visitados = []
    final = [[1,2,3],[4,5,6],[7,8,0]]
    sal = False
    estado = [i[:] for i in datos]
    espacio = []
    iteracioens = 0
    while not sal and iteracioens < 100000:
        if estado == final:
            return
        posiciones = sacarMovimentos(estado)
        print(posiciones)
        for x in posiciones:
            espacio.append(mover(estado,x))
        siguente = hacerMovimento(espacio,visitados,final)
        if siguente != -1:
            estado = siguente
            visitados.append(estado)
        else:
            if len(visitados) >= 2:
                estado = visitados[-2]
            elif len(visitados) == 1:
                estado = visitados[-1]
        iteracioens += 1
def Main():
    datos = LeerDatos('../Txt/numeros_magicos.txt')
    print(datos)
    algoritmo(datos)
Main()