# Búsqueda en lista ordenada:
# Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.

lista = [
    "banana",
    "durazno",
    "kiwi",
    "mandarina",
    "manzana",
    "melon",
    "naranja",
    "pera",
    "sandia",
    "uva",
]


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(lista, "pera"))
