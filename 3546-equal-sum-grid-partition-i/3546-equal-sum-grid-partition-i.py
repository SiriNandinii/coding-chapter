from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Check horizontal cuts
        curr = 0
        for i in range(n - 1):  # must leave bottom non-empty
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # Check vertical cuts
        curr = 0
        col_sums = [0] * m
        
        for j in range(m):
            for i in range(n):
                col_sums[j] += grid[i][j]
        
        for j in range(m - 1):  # must leave right non-empty
            curr += col_sums[j]
            if curr == target:
                return True
        
        return False