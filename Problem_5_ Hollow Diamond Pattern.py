#hollow diamond pattern

# Print the upper half of the diamond including the middle row
for i in range(5):
    print(" " * (5 - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")
    
# Print the lower half of the diamond
for i in range(5 - 2, -1, -1):
    print(" " * (5 - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")