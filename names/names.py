import time

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # first, we need to determine if the value is less or greater than self.value

    # If value is less than and there is not already a value on the left, assign value to left
    if self.value:
        if value < self.value:

            if not self.left:
                self.left = BinarySearchTree(value)
            # If there is a value on the left already, run insert recursively
            else:
                self.left.insert(value)

        # If value is greater than or equal to self.value, assign value to right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    else:
        self.value = value

  def contains(self, target):
    # Here we need to determine if the target can be found in the search tree
    if target == self.value:
      return self.value
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# dups = []
# for name in names_1:
#     dups.insert(name)

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if temp.contains(name_2)
#             duplicates.append(name_1)

# Possible solution - make a set out of the lists, and run intersection
# to return the duplicates of both lists
duplicates = set(names_1).intersection(set(names_2))
end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# We want to improve this runtime.
# We can do this with a binary search

# def search_for_dups(arr, left, right, x):
#     if right >= left:
#         mid = left + (right - left) / 2

