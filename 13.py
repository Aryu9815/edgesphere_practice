# 13.Group By Type
# a. Given: A list of mixed types.
# Return: A dictionary grouping values by their type.
# Example:
# Input: [1, "a", 2.5, "b"] → Output: {int: [1], str: ["a",
# "b"], float: [2.5]}

def group_by_type(l):
    d = {}
    for i in l:
        key = type(i).__name__
        d[key] = d.get(key,[])
        d[key].append(i)
    return d

print(group_by_type( [1, "a", 2.5, "b"] ))