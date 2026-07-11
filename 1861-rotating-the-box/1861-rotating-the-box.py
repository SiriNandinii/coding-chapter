class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Let stones fall to the right
        for row in boxGrid:
            empty = n - 1

            for col in range(n - 1, -1, -1):

                if row[col] == '*':
                    empty = col - 1

                elif row[col] == '#':
                    row[col], row[empty] = row[empty], row[col]
                    empty -= 1

        # Step 2: Rotate 90 degrees clockwise
        res = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res