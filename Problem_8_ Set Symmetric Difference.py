#define

def symmetric_difference(set1, set2):
    # Calculate the symmetric difference
    sym_diff = set1.symmetric_difference(set2)
    return sym_diff

# Sample Input
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Finding the symmetric difference
output = symmetric_difference(set1, set2)
print(output)


