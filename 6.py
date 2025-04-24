# 6. Flatten Nested List (use recursion)
# a. Given: A nested list of integers.
# Return: A flat list.
# Example:
# Input: [[1,2], [3,4]] → Output: [1, 2, 3, 4]

def nested_list(l):
    res = []
    for i in l:
        # here , if element is list then it extends to res
        if isinstance(i,list):
            res.extend(nested_list(i))
        else:
            res.append(i)
    return res

print(nested_list([[1,2],[1,2,2,3,4,[2,3,4,[5]]], [3,4]]))