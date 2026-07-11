from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = set()

        for r in range(m):
            for c in range(n):
                
                # radius 0 (single cell)
                rhombus_sums.add(grid[r][c])

                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    total = 0

                    # top → right
                    i, j = r-k, c
                    for t in range(k):
                        total += grid[i+t][j+t]

                    # right → bottom
                    i, j = r, c+k
                    for t in range(k):
                        total += grid[i+t][j-t]

                    # bottom → left
                    i, j = r+k, c
                    for t in range(k):
                        total += grid[i-t][j-t]

                    # left → top
                    i, j = r, c-k
                    for t in range(k):
                        total += grid[i-t][j+t]

                    rhombus_sums.add(total)
                    k += 1

        return sorted(rhombus_sums, reverse=True)[:3]