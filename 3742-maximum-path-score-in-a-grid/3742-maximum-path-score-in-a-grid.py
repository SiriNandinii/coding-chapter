class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        # dp[i][j][c] = max score at (i,j) with cost c
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        start_cost = 1 if grid[0][0] != 0 else 0
        
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):

                    if dp[i][j][c] == -1:
                        continue

                    # move down
                    if i + 1 < m:
                        nc = c + (1 if grid[i + 1][j] != 0 else 0)

                        if nc <= k:
                            dp[i + 1][j][nc] = max(
                                dp[i + 1][j][nc],
                                dp[i][j][c] + grid[i + 1][j]
                            )

                    # move right
                    if j + 1 < n:
                        nc = c + (1 if grid[i][j + 1] != 0 else 0)

                        if nc <= k:
                            dp[i][j + 1][nc] = max(
                                dp[i][j + 1][nc],
                                dp[i][j][c] + grid[i][j + 1]
                            )

        ans = max(dp[m - 1][n - 1])

        return ans if ans != -1 else -1