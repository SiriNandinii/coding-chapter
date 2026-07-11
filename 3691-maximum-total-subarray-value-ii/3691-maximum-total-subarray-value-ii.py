from heapq import heappush, heappop

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # log table
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        K = lg[n] + 1

        # sparse tables
        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        for j in range(1, K):
            length = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(
                    st_max[j - 1][i],
                    st_max[j - 1][i + length]
                )
                st_min[j][i] = min(
                    st_min[j - 1][i],
                    st_min[j - 1][i + length]
                )

        def range_value(l: int, r: int) -> int:
            length = r - l + 1
            j = lg[length]

            mx = max(
                st_max[j][l],
                st_max[j][r - (1 << j) + 1]
            )
            mn = min(
                st_min[j][l],
                st_min[j][r - (1 << j) + 1]
            )

            return mx - mn

        # max heap using negative values
        heap = []
        for l in range(n):
            val = range_value(l, n - 1)
            heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_val, l, r = heappop(heap)
            ans += -neg_val

            if r - 1 >= l:
                nxt = range_value(l, r - 1)
                heappush(heap, (-nxt, l, r - 1))

        return ans