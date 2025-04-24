# 17.Key Existence Checker
# a. Given: A dictionary and a key.
# Return: True if key exists, else False (without using in keyword).
# Example:
# Input: {"a":1}, "b" → Output: False

def existence_checker(d,key):
    return len(list(filter(lambda x:x==key,d.keys()))) == 1 

print(existence_checker({"a":1}, "a"))