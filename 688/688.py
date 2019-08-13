class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def isvalid(x, y):
            return (x >= 0 and x < N and y >= 0 and y < N)
        
        dx = [2, 2, 1, 1, -1, -1, -2, -2]
        dy = [1, -1, 2, -2, 2, -2, 1, -1]
        dp = [[[0 for _ in range(N)] for __ in range(N)] for ___ in range(2)]
        dp[0][r][c] = 1
        for i in range(1, K + 1):
            for r in range(N):
                for c in range(N):
                    if dp[(i-1) % 2][r][c] != 0:
                        # Calculate the L shape movements
                        for k in range(8):
                            nr = r + dx[k] #new row
                            nc = c + dy[k] #new col
                            if isvalid(nr, nc): #check to see if it is within bounds
                                if i == 0:
                                    dp[i % 2][nr][nc] += 1
                                else:
                                    # Calculate number of ways from last timestep
                                    dp[i % 2][nr][nc] += dp[(i-1) % 2][r][c]
            # Reset dp values so that old calculated values don't overflow, since we
            # are reusing the array
            for r in range(N):
                for c in range(N):
                    dp[(i - 1) % 2][r][c] = 0
        
        tot = 0
        for r in range(N):
            for c in range(N):
                tot += dp[K % 2][r][c]
        return float(tot) / (8**K)        
