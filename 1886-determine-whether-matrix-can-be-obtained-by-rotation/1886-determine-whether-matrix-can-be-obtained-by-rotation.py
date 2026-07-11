from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            # 90 degree clockwise rotation
            return [list(row) for row in zip(*matrix[::-1])]
        
        for _ in range(4):  # try all rotations
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False