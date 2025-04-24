# 3. List to Dictionary
# a. Given: Two lists, one of keys and one of values.
# Return: A dictionary mapping keys to values.
# Example:
# Input: ["a", "b"], [1, 2] → Output: {"a":1, "b":2}

def create_dictionary(l1,l2):
    
    return dict(zip(l1,l2))

print(create_dictionary(["a", "b"], [1, 2]))