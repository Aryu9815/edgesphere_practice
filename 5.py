# 5. Tuple Swap
# a. Given: A tuple (a, b)
# Return: A new tuple with values swapped.
# Example:
# Input: (5, 10) → Output: (10, 5)

def swapping(t):
    return (t[1],t[0])

print(swapping((5,10)))
print(type(swapping((5,10))))
