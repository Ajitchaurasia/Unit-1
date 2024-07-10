# Define Subset Verification:-

def is_subset(set1, set2):
    # Iterate through each element in set1
    for elem in set1:
        # If any element(elem) is not found in set2, so, return False
        if elem not in set2:
            return False
    # If all elements(elem) are found in set2, so, return True
    return True
# Input 
subset = {1, 2, 3} # potential subset
superset = {1, 2, 3, 4, 5, 6}

# Checking if subset is a subset of superset
result = is_subset(subset, superset)
print(result)
