from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions allowed for each street type
        street = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        
        while queue:
            r, c = queue.popleft()
            
            # Reached destination
            if r == m - 1 and c == n - 1:
                return True
            
            # Explore neighbors
            for dr, dc in street[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Check reverse connection
                    if (-dr, -dc) in street[grid[nr][nc]]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        
        return False