arr1 = ["100", "101", "101", "100", "100"]
arr2 = "1001"

for indice, elemento in enumerate(arr2):
    aux = arr1[indice]
    aux = aux[:-1] + elemento
    arr1[indice] = aux

print(arr1)
