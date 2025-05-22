from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = defaultdict(int)

        # find up to 2 potential major candidates
        # there can be at most 2 elements that appear more than n / 3 times
        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue        # move to the next num(skip pruning if we have 2 or fewer candidates)
            
            # prune the candidate set if we have more than 2
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:               # remove a candidate with count = 0
                    new_count[n] = c - 1
            count = new_count

        # check if the remaining major candidates occur more than n / 3 times
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res