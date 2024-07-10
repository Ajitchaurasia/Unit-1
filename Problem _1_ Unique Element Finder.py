def find_unique_elements(lst):
    # Create an empty dictionary to count occurrences of each element
    count_dict = {}
    
    # Count  each element
    for elem in lst:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    
    # Extract elements that occur only once
    unique_elements = [elem for elem, count in count_dict.items() if count == 1]
    
    print(unique_elements)
    
input_list = [1, 2, 2, 3, 4, 5, 3, 6, 4]
output = find_unique_elements(input_list)
print(output) 

