class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        ans = 0
        col_x = [0]*n
        col_y = [0]*n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    col_x[j] += 1
                elif grid[i][j] == 'Y':
                    col_y[j] += 1
            
            x = 0
            y = 0
            
            for j in range(n):
                x += col_x[j]
                y += col_y[j]
                
                if x == y and x > 0:
                    ans += 1
        
        return ans