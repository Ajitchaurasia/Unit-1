# diamond pattern

for i in range(3):
    print(" " * (3 - i - 1) + "*" * (2 * i + 1))
    
# Print the lower half of the diamond
for i in range(3- 2, -1, -1):
    print(" " * (3 - i - 1) + "*" * (2 * i + 1))