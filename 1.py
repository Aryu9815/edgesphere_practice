# 1. Character Frequency Counter
# a. Given: A string.
# Return: A dictionary with the frequency of each character.
# Example:
# Input: "hello" → Output: {'h':1, 'e':1, 'l':2, 'o':1}

def frequency_counter(s):
    d = {i:s.count(i) for i in s}
   
    print(d)

frequency_counter('heeello')