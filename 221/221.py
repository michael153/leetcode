class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    ans = 1
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] and i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    ans = max(ans, dp[i][j])
        return ans*ans
