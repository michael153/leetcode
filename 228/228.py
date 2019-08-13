class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                s = str(nums[start])
                if start + 1 != i:
                    s += ("->" + str(nums[i-1]))
                ranges += [s]
                start = i
        if len(nums) > 1 and nums[-1] == nums[-2] + 1:
            ranges += [(str(nums[start]) + "->" + str(nums[-1]))]
        else:
            ranges += [str(nums[-1])]
        return ranges
