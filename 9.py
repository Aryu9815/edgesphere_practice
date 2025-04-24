# 9. String Compression
# a. Given: A string, compress repeated characters as counts.
# Example:
# Input: "aaabbc" → Output: "a3b2c1"

def string_compression(s):
    l = []
    i = 0
    while i <len(s):
        c = 1
        char = s[i]
        while i+1 < len(s) and s[i] == s[i+1]:
                c+=1
                i+=1
        l.append(char)
        l.append(str(c))
        i += 1
    return ''.join(l)
print(string_compression('aaabbbaabcc'))