# 16.Longest Word
# a. Given: A string containing multiple words.
# Return: The longest word.
# Example:
# Input: "This is OpenAI GPT" → Output: "OpenAI"

def longest_word(s):
    return ''.join(filter(lambda x:len(x.strip()) == max(map(lambda x:len(x.strip()),s.strip().split())),s.strip().split()))

print(longest_word( "This is OpenAI GPT"))