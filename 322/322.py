class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {}
        inf = 1e9

        dp[amount] = inf
        dp[0] = 0
        coins.sort()
        
        for amt in range(1, amount + 1):
            if amt not in dp:
                dp[amt] = inf
            for coin in coins:
                if coin > amt:
                    break
                dp[amt] = min(dp[amt - coin] + 1, dp[amt])
        
        return -1 if dp[amount] == inf else dp[amount]
