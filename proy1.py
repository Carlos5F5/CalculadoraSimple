# FUNCION PARA QUE ENCUENTRE EL NÚMERO MÁS REPETIDO EN UNA LISTA

def mas_repetido(nums):
    cont = {}

    for num in nums:
        if num in cont:
            cont[num] += 1
        else:
            cont[num] = 1

    max_num = 0
    max_rep = 0

    for num, rep in cont.items():
        if rep > max_rep:
            max_rep = rep
            max_num = num

    return max_num, max_rep

# Lista para probar
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 4, 4, 4, 5]

# Llamar a la función y mostrar resultados
numero, repeticiones = mas_repetido(nums)

print(f"El número más repetido es {numero} y se repite {repeticiones} veces.")
