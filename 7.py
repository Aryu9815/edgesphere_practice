# 7. Anagram Check
# a. Given: Two strings.
# Return: True if they are anagrams, else False.
# Example:
# Input: "listen", "silent" → Output: True

def anagrams(s1,s2):
    return len(s1) == len(s2) and len(list(filter(lambda x: x not in s2.lower(),s1.lower())))==0  

print(anagrams('listen','silent'))

