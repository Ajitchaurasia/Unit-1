
def print_tree(height):
  """Prints a Christmas tree pattern using * 

  Args:
    height: The height of the tree in rows.
  """

  for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

  trunk_spaces = " " * (height - 1)
  print(trunk_spaces + "|")

height = int(input("Enter the height of the tree: "))
print_tree(height)


