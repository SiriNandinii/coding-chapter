from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Next expected value: 1 → 2 → 0 → 2 → 0 …
        def next_val(x):
            return 2 if x == 1 else (0 if x == 2 else 2)
        
        def in_bounds(i, j):
            return 0 <= i < m and 0 <= j < n
        
        directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        
        @cache
        def dfs(i: int, j: int, di: int, dj: int, turned: bool) -> int:
            # Start from grid[i][j], assumed valid
            val = grid[i][j]
            nxt = next_val(val)
            length = 1  # include current
            
            # Continue straight
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj) and grid[ni][nj] == nxt:
                length = 1 + dfs(ni, nj, di, dj, turned)
            
            # If a turn is still allowed, try one clockwise turn
            if not turned:
                # clockwise: (di, dj) → (dj, -di)
                tdi, tdj = dj, -di
                ti, tj = i + tdi, j + tdj
                if in_bounds(ti, tj) and grid[ti][tj] == nxt:
                    length = max(length, 1 + dfs(ti, tj, tdi, tdj, True))
            return length
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        answer = max(answer, dfs(i, j, di, dj, False))
        
        return answer
