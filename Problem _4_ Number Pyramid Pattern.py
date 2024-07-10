#number pyramind pattern
 # Iterate through each level of the pyramid
for i in range(1, 4 + 1):
    print(" " * (4 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
