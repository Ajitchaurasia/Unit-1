# define set difference for more than two sets :--

def set_difference(*sets):
    if not sets:
        return set()
    
    # Initi  the difference set with the first set
    difference = sets[0].copy()
    # Iterate through each element in the first set
    for elem in sets[0]:
        # Check if the element is present in any of the other sets
        if any(elem in s for s in sets[1:]):
            difference.remove(elem)
    return difference
# Sample Input
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
set3 = {50, 60, 90} 
# Finding the set difference
result = set_difference(set1, set2, set3)
print(result)
 