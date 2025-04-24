# 10.Dict Merge
# a. Given: Two dictionaries.
# Return: A merged dictionary. In case of conflicts, values from the second
# dictionary should overwrite.
# Example:
# Input: {"a": 1}, {"a": 2, "b": 3} → Output: {"a": 2, "b": 3}

def dict_merged(d1,d2):
    d1.update(d2)
    return d1

print(dict_merged({"a": 1}, {"a": 0, "b": 3}))