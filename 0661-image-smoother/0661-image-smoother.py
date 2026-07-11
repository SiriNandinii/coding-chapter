class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        ans = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                total = 0
                count = 0

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < m and 0 <= nc < n:
                            total += img[nr][nc]
                            count += 1

                ans[r][c] = total // count

        return ans