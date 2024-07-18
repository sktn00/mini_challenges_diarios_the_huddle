# Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.
def remove_duplicates_preserve_order(numbers):
    seen = set()
    return [x for x in numbers if not (x in seen or seen.add(x))]


# Test the function
original_list = [3, 7, 1, 4, 3, 9, 2, 7, 5, 1]
print("Original list:", original_list)

result = remove_duplicates_preserve_order(original_list)
print("List after removing duplicates (order preserved):", result)
print("Number of unique elements:", len(result))
