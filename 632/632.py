import bisect
import heapq

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

            pq = [(nums[i][ptr[i]], i) for i in range(K)]
            heapq.heapify(pq)

            smallest = pq[0][1]
            largest = heapq.nlargest(1, pq)[0][1]

            min_range = [nums[smallest][ptr[smallest]], nums[largest][ptr[largest]]]
            done = False

            while not done:
                left, right = nums[smallest][ptr[smallest]], nums[largest][ptr[largest]]
                mag = right - left
                min_mag = min_range[1] - min_range[0]

                if mag < min_mag:
                    min_range = [left, right]
                if mag == min_mag and left < min_range[0]:
                    min_range = [left, right]

                ptr[smallest] += 1
                if ptr[smallest] == len(nums[smallest]):
                    done = True
                    break

                payload = (nums[smallest][ptr[smallest]], smallest)
                heapq.heappushpop(pq, payload)

                if payload[0] >= nums[largest][ptr[largest]]:
                    largest = smallest

                smallest = pq[0][1]

        return min_range
