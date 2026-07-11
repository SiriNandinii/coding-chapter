class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [0] * n
        ans = 0
        
        for i in range(m):
            # update histogram heights
            for j in range(n):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0
            
            # count submatrices using monotonic stack
            stack = []
            sum_row = 0
            for j in range(n):
                cnt = 1
                while stack and stack[-1][0] >= height[j]:
                    h, c = stack.pop()
                    sum_row -= h * c
                    cnt += c
                stack.append((height[j], cnt))
                sum_row += height[j] * cnt
                ans += sum_row
        
        return ans

        