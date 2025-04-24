# 14.JSON Key Extractor
# a. Given: A nested dictionary.
# Return: All keys at all levels in a flat list.
# Example:
# Input: {"a": 1, "b": {"c": 2}} → Output: ["a", "b", "c"]

def key_extractor(d):
    l = []
    for k,v in d.items():
        if isinstance(v,dict):
            l.append(k)
            l.extend(key_extractor(v))
        else:
            l.append(k)
    return l
print(key_extractor( {"a": 1, "b": {"c": 2}}))