#define tuple reversal not useing inbuit funcation:-

def reverse_tuple(input_tuple):
    # Convert the tuple to a list to reverse the elements 
    temp_list = list(input_tuple)
    # Initialize an empty list to store the reversed elements
    reversed_list = []
    # Loop through the elements of the temp_list in reverse order
    for i in range(len(temp_list) - 1, -1, -1):
        reversed_list.append(temp_list[i])
    # Convert the reversed list back to a tuple
    reversed_tuple = tuple(reversed_list)
    return reversed_tuple
# Sample input tu
input_tuple = (1, 2, 3, 4, 5)
# Reverse the tuple
reversed_result = reverse_tuple(input_tuple)
# Print the result
print(reversed_result)

