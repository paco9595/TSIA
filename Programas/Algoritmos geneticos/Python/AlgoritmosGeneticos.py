import csv

def ValidarDatos(datos):
		for row in datos:
			for cell in row:
				if (cell == '0') or (cell == '1'):
					return True
				else: 
					return False

def LeerDatos():
	try:
		datos = []
		auxRow = []
		with open('Datos.csv', 'rt') as csvfile:
			Archivo = csv.reader(csvfile, delimiter=',')
			for row in Archivo:
				for cell in row:
					auxRow.append(cell)
				datos.append(auxRow)
		if ValidarDatos(datos):
			return datos		
	except IOError:
		print ("Archivo no encontrado o en formato incorrecto, revise que sea de tipo CSV")
		return

		
def main():
	datos = LeerDatos()
	print (datos)
main()