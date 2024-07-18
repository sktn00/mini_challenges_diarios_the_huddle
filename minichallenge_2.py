# Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento
# que prefieras (por ejemplo, burbuja, inserción, selección).
lista = [32, 10, 51, 26, 42]


def find_smallest(arr):
    smallest = arr[0]  # -> Stores the smallest value
    smallest_index = 0  # -> Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):  # -> Sorts an array / list
    nueva_lista = []
    copied_arr = list(arr)  # copy array before mutating
    for i in range(len(copied_arr)):
        smallest = find_smallest(
            copied_arr
        )  # -> Find the smallest element in the array and
        nueva_lista.append(copied_arr.pop(smallest))  # adds it to the new array
    return nueva_lista


print(selection_sort(lista))
