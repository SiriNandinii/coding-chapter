from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        divCnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for m in range(g, mx + 1, g):
                divCnt[g] += freq[m]
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = divCnt[g]
            total = c * (c - 1) // 2

            m = 2 * g
            while m <= mx:
                total -= exact[m]
                m += g

            exact[g] = total
        prefix = []
        values = []

        cur = 0
        for g in range(1, mx + 1):
            if exact[g]:
                cur += exact[g]
                prefix.append(cur)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans