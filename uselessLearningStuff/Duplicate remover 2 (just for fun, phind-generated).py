def remove_duplicates_ordered(iterable):
    seen = set()
    unique_iterable = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            unique_iterable.append(item)
    return unique_iterable

# Example usage
my_list = [1, 2, 3, 2, 4, 5, 3, 6]
print("Original list:", my_list)

# Remove duplicates while preserving order
no_duplicates_list = remove_duplicates_ordered(my_list)
print("List without duplicates (ordered):", no_duplicates_list)