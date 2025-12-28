s = 'ransome'
hash_map = {}
for char in s:
    if char in hash_map:
        hash_map[char] += 1
    else:
        hash_map[char] = 1
print(hash_map)        