#define
def difference_between_sets(set1, set2):
    # Calculate the difference
    difference = set1.difference(set2)
    return difference

# Sample Input
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

# Finding the difference
output = difference_between_sets(set1, set2)
print(output)
