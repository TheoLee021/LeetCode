from collections import defaultdict

class Solution(object):
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