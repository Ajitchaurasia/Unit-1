#define union and intersection:
def set_operations(set1, set2):
    # Calculate union
    union_set = set1.union(set2)
    
    # Calculate intersection
    intersection_set = set1.intersection(set2)
    
    print(union_set, intersection_set)
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    union_result, intersection_result = set_operations(set1, set2)
    print("Union:", union_result)
    print("Intersection:", intersection_result) 

