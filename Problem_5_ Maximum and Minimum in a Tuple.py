# define Maximum and Minimum in a Tuple :-

def find_max_min(numbers):
    # Initia max and min with the first element of the tuple
    max_num = numbers[0]
    min_num = numbers[0]
    # Iterate through the tuple starting from the second element
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num
#  Input
numbers = (5, 10, 3, 15, 2, 20)

# Find the maximum and minimum numbers
max_num, min_num = find_max_min(numbers)
print( max_num)
print( min_num)
