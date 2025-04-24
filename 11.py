# 11. Intersection of Sets
# a. Given: Two lists.
# Return: A list of common elements (no duplicates).
# Example:
# Input: [1, 2, 3], [2, 3, 4] → Output: [2, 3]

def set_intersection(l1,l2):
    return set(l1).intersection(l2)

print(set_intersection([1, 2, 3], [2, 3, 4]))