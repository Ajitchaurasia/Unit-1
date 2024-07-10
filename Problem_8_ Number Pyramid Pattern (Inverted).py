# number pyramind pattern interted
size=5

# Print leading spaces for alignment
for i in range(size, 0, -1):
    print(" " * (size - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")  # Move to the next line after each row
    print()