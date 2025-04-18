def busqueda_lineal(arr, objetivo):
    for i, val in enumerate(arr):
        if val == objetivo:
            return i
    return -1

print(busqueda_lineal([1,2,3], 2))