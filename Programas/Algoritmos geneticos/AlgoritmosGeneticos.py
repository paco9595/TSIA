import csv
#enconding: utf-8

#Funcion utilizada para leer un archivo de tipo csv
def LeerDatos():
	try:
		datos = []
		with open('TestVacio.csv', 'rt') as csvfile:
			Archivo = csv.reader(csvfile, delimiter=' ', quotechar='|')
			print ("Datos originales:\n")
			for row in Archivo:
				datos.append(row)
				print (row)
		return datos
	except IOError:
		print ("Archivo no encontrado o en formato incorrecto, revise que sea de tipo CSV")
		return
		
def main():
	datos = LeerDatos()
	
if __name__ == "__main__": main()