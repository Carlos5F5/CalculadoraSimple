frase = "Las mejores cosas en la vida son gratis"
print((frase))
print(len(frase))
slicing = frase[0:3]
print(slicing)
clave = input("Ingrese una palabra que se encuentra en la frase: ")
if clave in frase:
	print("La palabra " , clave,  " está presente en la frase.")
else:
	print("La palabra ", clave,  " no está presente en la frase.")