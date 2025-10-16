# sort
def topKFrequent(nums, k):
    hashmap = {}

    for num in nums:
        hashmap[num] = 1 + hashmap.get(num, 0)

    arr = []
    for num, freq in hashmap.items():
        arr.append([freq, num])
    arr.sort()
    print(arr)

    i = 0
    result = []
    while i < k:
        result.append(arr.pop()[1])
        i += 1

    return result

print(topKFrequent([1,1,1,2,3,3], 2))