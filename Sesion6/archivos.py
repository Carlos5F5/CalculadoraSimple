#Trabajando con archivos
try:
	archivo = open(r".\ejemploarchivos.txt", "r")
	contenido = archivo.read()
	archivo.close()
	print(contenido)
except FileNotFoundError:
	print("El archivo 'ejemploarchivos.txt' no se encontró. Por favor, verifica su existencia.")

