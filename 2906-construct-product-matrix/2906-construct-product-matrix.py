from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        size = n * m
        res = [1] * size
        
        # Step 1: prefix
        prefix = 1
        for i in range(size):
            r, c = divmod(i, m)
            res[i] = prefix
            prefix = (prefix * grid[r][c]) % MOD
        
        # Step 2: suffix
        suffix = 1
        for i in range(size - 1, -1, -1):
            r, c = divmod(i, m)
            res[i] = (res[i] * suffix) % MOD
            suffix = (suffix * grid[r][c]) % MOD
        
        # Step 3: convert back to 2D
        ans = [[0]*m for _ in range(n)]
        for i in range(size):
            r, c = divmod(i, m)
            ans[r][c] = res[i]
        
        return ans