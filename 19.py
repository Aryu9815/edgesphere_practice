# 19.Replace Elements with Greatest on Right
# a. Given: A list of integers.
# Return: A list where each element is replaced with the greatest element
# among the elements to its right. The last element should be -1.
# Example:
# Input: [17, 18, 5, 4, 6, 1] → Output: [18, 6, 6, 6, 1, -1]

def greatest_on_right(l):
    # for i in range(len(l)):
    #     if i == len(l)-1:
    #         l[i] = -1
    #         continue
    #     l[i] = max(l[i+1:])
    return list(map(lambda x: max(l[x+1:]) if x+1 < len(l) else -1, range(len(l))))

print(greatest_on_right([17, 18, 5, 4, 6, 1]))
