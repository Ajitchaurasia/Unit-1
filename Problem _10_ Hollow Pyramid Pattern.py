# Problem 10: Hollow Pyramid Pattern
size=5

for i in range(size - 1):
    # Print leading spaces
    print(" " * (size - i - 1), end="")
    # Print the first asterisk
    print("*", end="")
    if i > 0:
        print(" " * (2 * i - 1), end="")
        print("*", end="")
    print()
    
# Print the last row with all asterisks
print("*" * (2 * size - 1))