#define

def remove_duplicates_and_sort(lst):
    unique_elements = set(lst)
    
    # Convert the set back to a list and sort it in ascending order
    sorted_unique_list = sorted(unique_elements)
    # Convert the sorted list to a tuple
    result_tuple = tuple(sorted_unique_list)
    return result_tuple

# Sample Input
input_list = [1, 2, 3, 4, 3, 2, 1]

# Removing duplicates and sorting the list
output_tuple = remove_duplicates_and_sort(input_list)
print(output_tuple)
