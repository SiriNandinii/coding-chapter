from typing import List
from math import inf
from functools import lru_cache

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def f(i1: int, j1: int, i2: int, j2: int) -> int:
            imin = jmin = inf
            imax = jmax = -inf
            for i in range(i1, i2 + 1):
                for j in range(j1, j2 + 1):
                    if grid[i][j] == 1:
                        imin = min(imin, i)
                        jmin = min(jmin, j)
                        imax = max(imax, i)
                        jmax = max(jmax, j)
            if imax == -inf:
                return 0
            return (imax - imin + 1) * (jmax - jmin + 1)

        ans = m * n  # upper bound

        # 1) Horizontal partitions
        for i1 in range(m - 2):
            for i2 in range(i1 + 1, m - 1):
                ans = min(ans,
                          f(0, 0, i1, n - 1) +
                          f(i1 + 1, 0, i2, n - 1) +
                          f(i2 + 1, 0, m - 1, n - 1))

        # 2) Vertical partitions
        for j1 in range(n - 2):
            for j2 in range(j1 + 1, n - 1):
                ans = min(ans,
                          f(0, 0, m - 1, j1) +
                          f(0, j1 + 1, m - 1, j2) +
                          f(0, j2 + 1, m - 1, n - 1))

        # 3) Mixed partitions
        for i in range(m - 1):
            for j in range(n - 1):
                # top split into 2, bottom remains one
                ans = min(ans,
                          f(0, 0, i, j) +
                          f(0, j + 1, i, n - 1) +
                          f(i + 1, 0, m - 1, n - 1))

                ans = min(ans,
                          f(0, 0, i, n - 1) +
                          f(i + 1, 0, m - 1, j) +
                          f(i + 1, j + 1, m - 1, n - 1))

                # left split into 2, right remains one
                ans = min(ans,
                          f(0, 0, i, j) +
                          f(i + 1, 0, m - 1, j) +
                          f(0, j + 1, m - 1, n - 1))

                ans = min(ans,
                          f(0, 0, m - 1, j) +
                          f(0, j + 1, i, n - 1) +
                          f(i + 1, j + 1, m - 1, n - 1))

        return ans
