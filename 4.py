# 4. Find Unique Integers
# a. Given: A list of integers where every element appears twice except one.
# Return: That unique element.
# Example:
# Input: [2, 2, 1] → Output: 1


nums = [4, 1, 2, 1, 2, 4, 7]

def unique_element(l):
    
    # it returns the element with count 1
    return list(filter(lambda x: l.count(x)==1,l))[0]

print(unique_element(nums))