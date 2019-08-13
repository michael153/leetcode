class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        lengths = [1, 7, 30]
        
        def b_intersect(arr, val):
            lo, hi = 0, len(arr)
            mid = (lo + hi) / 2
            while lo < hi:
                if arr[mid] == val:
                    return mid
                elif arr[mid] < val and (mid + 1 == len(arr) or arr[mid + 1] > val):
                    return mid + 1
                elif arr[mid] > val:
                    hi = mid
                else:
                    lo = mid + 1
                mid = (lo + hi) / 2
            return mid
        
        inf = 1e9
        dp = {}
                
        def solve(index):
            days_left = len(days) - index
            if days_left <= 0:
                return 0
            if days_left == 1:
                return min(costs)
            if days_left not in dp:
                dp[days_left] = inf
            else:
                return dp[days_left]
            for i, l in enumerate(lengths):
                nxt = b_intersect(days, days[index] + l)
                ret = costs[i] + solve(nxt)
                dp[days_left] = min(ret, dp[days_left])
            return dp[days_left]
                
        return solve(0)
