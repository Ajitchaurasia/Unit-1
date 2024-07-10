#define set union 
def union_of_sets(set1, set2, set3):
    result_set = set()
# Add elements from set1 to set3 result_set
    for element in set1:
        result_set.add(element)    
    for element in set2:
        result_set.add(element)
    for element in set3:
        result_set.add(element)
        
    return result_set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
result = union_of_sets(set1, set2, set3)
print(result)
