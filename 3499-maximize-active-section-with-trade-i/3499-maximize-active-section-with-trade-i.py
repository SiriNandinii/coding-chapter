class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        totalOnes = s.count('1')

        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        ans = totalOnes
        m = len(runs)

        for i in range(1, m - 1):
            if (
                runs[i][0] == '1'
                and runs[i - 1][0] == '0'
                and runs[i + 1][0] == '0'
                and i - 2 >= 0
                and i + 2 < m
                and runs[i - 2][0] == '1'
                and runs[i + 2][0] == '1'
            ):
                merged = runs[i - 1][1] + runs[i][1] + runs[i + 1][1]
                ans = max(ans, totalOnes - runs[i][1] + merged)

        return min(ans, len(s))