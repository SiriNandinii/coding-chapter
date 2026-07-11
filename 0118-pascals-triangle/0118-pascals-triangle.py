class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [0] * (i + 1)
            for j in range(i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = res[-1][j-1] + res[-1][j]
            res.append(row)
            
        return res 