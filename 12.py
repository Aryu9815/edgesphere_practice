# 12.Reverse Mapping
# a. Given: A dictionary.
# Return: A new dictionary with keys and values swapped.
# Example:
# Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"}

def reverse_mapping(d):
    return {k:v for v,k in d.items()}

print(reverse_mapping({"a": 1, "b": 2}))