from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        heights = [0] * n
        ans = 0
        
        for r in range(m):
            
            # build histogram heights
            for c in range(n):
                if matrix[r][c] == 0:
                    heights[c] = 0
                else:
                    heights[c] += 1
            
            # we can reorder columns → sort heights
            sorted_heights = sorted(heights, reverse=True)
            
            for i in range(n):
                area = sorted_heights[i] * (i + 1)
                ans = max(ans, area)
        
        return ans