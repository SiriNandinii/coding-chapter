from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        comp = [0] * n

        for i in range(1, n):
            comp[i] = comp[i - 1]
            if nums[i] - nums[i - 1] > maxDiff:
                comp[i] += 1

        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans