#define Intersection of Multiple Sets:-

def intersection_of_sets(*sets):
    if not sets:
        return set()
    
    # Initialize the intersection set  set1
    intersection = sets[0].copy()
    
    # Iterate through the elements(elem) of the initial set
    for elem in sets[0]:
        # Check if the element is present in all other sets
        if not all(elem in s for s in sets[1:]):
            intersection.remove(elem)
    
    return intersection
# Input
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set3 = {4, 5, 8, 9}
# Find the intersection

result = intersection_of_sets(set1, set2, set3)
print(result)
