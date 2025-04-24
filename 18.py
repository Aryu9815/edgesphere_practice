# 18.Safe List Index
# a. Given: A list and an index.
# Return: Element at the index or "Index Out of Range" safely.
# Example:
# Input: [1, 2, 3], 5 → Output: "Index Out of Range"

def safe_list_index(l,n):
    try:
        return l[n]
    except Exception as e:
        return e

print(safe_list_index([1, 2, 3], 2))