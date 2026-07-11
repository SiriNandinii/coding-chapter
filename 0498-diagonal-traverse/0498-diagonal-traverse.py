from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 means upward-right, -1 means downward-left

        for _ in range(m * n):
            result.append(mat[row][col])
            
            # Move in current direction
            if direction == 1:  # going up-right
                if col == n - 1:      # hit last column
                    row += 1
                    direction = -1
                elif row == 0:        # hit first row
                    col += 1
                    direction = -1
                else:                 # normal move
                    row -= 1
                    col += 1
            else:  # going down-left
                if row == m - 1:      # hit last row
                    col += 1
                    direction = 1
                elif col == 0:        # hit first column
                    row += 1
                    direction = 1
                else:                 # normal move
                    row += 1
                    col -= 1
        
        return result
