import bisect

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
        def findClosest(arr, target):
            return bisect.bisect_right(arr, target) - 1
                    
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((difficulty[i], profit[i]))
        jobs = sorted(jobs, key=lambda x: x[0])
        dp = [0 for i in range(len(difficulty))]
        difficulty = sorted(difficulty)
        profit = 0
        for i in range(len(jobs)):
            dp[i] = jobs[i][1]
            if i - 1 >= 0:
                dp[i] = max(dp[i], dp[i-1])
        for w in worker:
            closest = findClosest(difficulty, w)
            if closest != -1:
                profit += dp[closest]
        return profit
