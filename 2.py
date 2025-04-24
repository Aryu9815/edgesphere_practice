# 2. Valid Palindrome
# a. Given: A string.
# Return: True if it is a palindrome, ignoring non-alphanumeric and case; else
# False.
# Example:
# Input: "A man, a plan, a canal: Panama" → Output: True

def check_pallindrome(s):
    # it gives string with only alphanumeric characters
    s = ''.join(filter(lambda x:x.isalnum(),s)).lower()
    return s == s[::-1]

print(check_pallindrome("A man, a plan, a canal: Panama"))