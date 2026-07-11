from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = []
        
        # Flatten grid
        for row in grid:
            arr.extend(row)
        
        # Check feasibility
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        # Sort
        arr.sort()
        
        # Median
        median = arr[len(arr)//2]
        
        # Count operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops