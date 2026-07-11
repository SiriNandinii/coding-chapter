class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        # swap rows inside the square
        for i in range(k // 2):
            for j in range(k):
                # swap elements vertically
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
                grid[x + k - 1 - i][y + j], grid[x + i][y + j]
        
        return grid