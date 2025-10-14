# Sorting

from collections import defaultdict

def groupAnagrams(strs):
    hashmap = defaultdict(list)

    for s in strs:
        sorted_s = ''.join(sorted(s))
        hashmap[sorted_s].append(s)

    return list(hashmap.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))