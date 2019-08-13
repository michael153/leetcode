class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                hashmap[num].append(i)
            else:
                hashmap[num] = [i]
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and (i not in hashmap[comp] or len(hashmap[comp]) > 1):
                return [i, hashmap[comp][-1]]
