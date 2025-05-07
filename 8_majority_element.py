from collections import defaultdict

class Solution_hashmap(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > maxCount:
                res = num
                maxCount = hashmap[num]
        return res
    
class Solution_boyer_moore(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res