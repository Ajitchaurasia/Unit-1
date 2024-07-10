#Problem 9: Hollow Right Triangle Pattern
rows=5
for i in range(1, rows):
    if i == rows- 1:
# Print the last row with all asterisks
        print("*" * rows)
    else:
# Print the asterisks with spaces in between
        print("*" + " " * (i - 1) + "*")