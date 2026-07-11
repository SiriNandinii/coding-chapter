import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonals = []
        areas = []

        max_diag_value = 0
        max_diag_index = 0
        
        for i in range(len(dimensions)):
            diag = dimensions[i][0]**2 + dimensions[i][1]**2
            diag = math.sqrt(diag)
            ar = dimensions[i][0]*dimensions[i][1]
            
            areas.append(ar)
            diagonals.append(diag)

            if diag > max_diag_value:
                max_diag_value = diag
                max_diag_index = i
            
            if diag == max_diag_value:
                if areas[i] > areas[max_diag_index]:
                    max_diag_value = diag
                    max_diag_index = i                    

        return areas[max_diag_index] 