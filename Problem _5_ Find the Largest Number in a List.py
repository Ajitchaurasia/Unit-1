#define

def find_largest_number(lst):
    # Check if the list is empty
    if not lst:
        return None
    # Initialize the largest number with the first element of the list
    largest = lst[0]
    #the list to find the largest number
    for number in lst:
        if number > largest:
            largest = number
    return largest

# Sample Input
input_list = [4, 65, 32, 2, 104, 78, 10]

# Finding the largest number
largest_number = find_largest_number(input_list)

# Displaying the output
print(largest_number)

