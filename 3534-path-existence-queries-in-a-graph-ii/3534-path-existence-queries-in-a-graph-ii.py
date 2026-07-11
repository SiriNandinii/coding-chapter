from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort nodes by value
        order = sorted(range(n), key=lambda i: nums[i])
        vals = [nums[i] for i in order]

        # Position of each original node in the sorted order
        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        # Component ids (split where consecutive gap > maxDiff)
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # nxt[i] = furthest sorted index reachable in one edge
        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j
            if j == i:
                j += 1

        # Binary lifting
        LOG = n.bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            pu, pv = pos[u], pos[v]

            if pu == pv:
                ans.append(0)
                continue

            l, r = sorted((pu, pv))

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            cur = l
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    steps += 1 << k
                    cur = up[k][cur]

            ans.append(steps + 1)

        return ans