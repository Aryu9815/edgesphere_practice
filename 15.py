# 15.Most Frequent Value
# a. Given: A list of values.
# Return: The value that appears most frequently.
# Example:
# Input: [1,2,2,3] → Output: 2

def frequent_value(l):
    return sorted(zip((list(map(lambda x: l.count(x),l))),l),reverse=True)[0][1]

print(frequent_value([1,2,2,3,3,3]))