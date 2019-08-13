class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        mod = (10**9 + 7)
        dp = [[0 for __ in range(G + 1)] for ___ in range(P+1)]
        dp[0][0] = 1
       
        for c in range(len(group)):
            freeze = [r[:] for r in dp]
            reqppl = group[c]
            prof = profit[c]
            for k in range(P + 1):
                for p in range(G - reqppl, -1, -1):
                    b = min(k + prof, P)
                    freeze[b][p + reqppl] += (dp[k][p] % mod)
                    freeze[b][p + reqppl] %= mod
            dp = freeze
                
        ans = 0
        for p in range(G + 1):
            ans += dp[P][p]
            ans %= mod
        return ans
