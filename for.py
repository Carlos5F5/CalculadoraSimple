tupla = ("uno", "dos", "tres", "cuatro", "cinco")
print(tupla)
print(type(tupla))
print(len(tupla))

for i in tupla:
    print(i) # Imprime cada elemento de la tupla
n = 1
for e in tupla:
    print(f"Elemento {n}: {e}")
    n += 1