import csv

def ValidarDatos(row):
	if ():
		return False
	else:
		return False

def LeerDatos():
	try:
		datos = []
		with open('Datos.csv', 'rt') as csvfile:
			Archivo = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in Archivo:
				if (ValidarDatos(row)):
					datos.append(row)
				else:
					print ('Los datos contenidos en el CSV son erroneos, solo se admite 1 o 0')
					return
		return datos
	except IOError:
		print ("Archivo no encontrado o en formato incorrecto, revise que sea de tipo CSV")
		return

		
def main():
	datos = LeerDatos()
	if not (datos == ""):
		print ("Datos ingresados:\n")
		for row in datos:
			print (row)
	
main()