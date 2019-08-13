import bisect

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        K = len(nums)
        nums = sorted(nums, key = lambda l: l[0])
        # Get rid of duplicates
        for i in range(len(nums)):
            nums[i] = sorted(list(set(nums[i])))
        if K == 1:
            return [nums[0][0], nums[0][0]]
        else:
            ptr = [0 for _ in range(K)]
            ranks = [(nums[i][ptr[i]], i) for i in range(K)]
            ranks = sorted(ranks, key = lambda l: l[0])

            smallest = ranks[0][1]
            largest = ranks[-1][1]

            min_range = [nums[smallest][ptr[smallest]], nums[largest][ptr[largest]]]

            while True:
                left, right = nums[smallest][ptr[smallest]], nums[largest][ptr[largest]]
                mag = right - left
                min_mag = min_range[1] - min_range[0]

                if mag < min_mag:
                    min_range = [left, right]
                if mag == min_mag and left < min_range[0]:
                    min_range = [left, right]

                ptr[smallest] += 1
                if ptr[smallest] == len(nums[smallest]):
                    break

                ranks = ranks[1:]
                payload = (nums[smallest][ptr[smallest]], smallest)
                ranks.insert(bisect.bisect_left(ranks, payload), payload)

                smallest = ranks[0][1]
                largest = ranks[-1][1]

        return min_range


a = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
ans = a.smallestRange(nums)

print(ans)
