#define

def check_element_in_tuple(tpl, elem):
    if elem in tpl:
        return True
    else:
        return False

# Sample Input
input_tuple = (10, 9, 8, 7, 6, 5)
element_to_check = 9

element_exists = check_element_in_tuple(input_tuple, element_to_check)
print(element_exists)

