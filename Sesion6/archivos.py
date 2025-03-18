#Trabajando con archivos
archivo = open("ejemploarchivos.txt", "r")
contenido = archivo.read()
archivo.close() 

print(contenido)

