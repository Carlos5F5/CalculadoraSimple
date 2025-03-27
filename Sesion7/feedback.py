#Trabajando con funciones/metodos

#Extracto de código  / script,  sirve para ejecutar procesos y retornar valores


#Creamos una funcion don def seguido de el nombre de la funcion

#Las funciones representan las acciones de la realidad

def caminar():
    #print("La persona está caminando")
    return "La persona está caminando"
def reir():
    print("La persona está riendo")

def dormir():
    print("La persona está durmiendo")

#Para ejecutar la funcion se escribe el nombre de la funcion seguido de parentesis
#Se tiene que invocar/llamar a la funcion para que se ejecute

def suma(valor1, valor2, valor3):
    r = valor1 + valor2 + valor3
    p = r / 3
    return r

try:
    n1 = int(input("Ingrese número 1: "))
    n2 = int(input("Ingrese número 2: "))
    n3 = int(input("Ingrese número 3: "))
    r = suma(n1, n2, n3)
   
except:
    print("Error: Ingrese solo números")
    

print ("El resultado de la suma es: ", r)
print ("El promedio de la suma es: ", r/3)
    
print(caminar())
reir()
dormir()


