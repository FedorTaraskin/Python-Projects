def remove_duplicates(iterable):
    # Convert the iterable to a set to remove duplicates
    unique_set = set(iterable)
    
    # Convert the set back to the original type of the iterable
    # For example, if the input was a list, we convert the set back to a list
    unique_iterable = list(unique_set)
    
    return unique_iterable

# Example usage
my_list = [1, 2, 3, 2, 4, 5, 3, 6]
print("Original list:", my_list)

# Remove duplicates
no_duplicates_list = remove_duplicates(my_list)
print("List without duplicates:", no_duplicates_list)