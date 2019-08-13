class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        front = 1
        back = N - 2
        ret = [1]*N
        fmult = [1, 1]
        bmult = [1, 1]
        while back >= 0 and front < N:
            fmult = (nums[front - 1]*fmult[0], fmult[0])
            bmult = (nums[back + 1]*bmult[0], bmult[0])
            ret[front] *= fmult[0]
            ret[back] *= bmult[0]
            front += 1
            back -= 1
        return ret
