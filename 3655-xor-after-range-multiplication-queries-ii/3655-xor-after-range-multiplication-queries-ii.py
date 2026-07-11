class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        import math
        B = int(math.sqrt(n)) + 1

        mul = [1] * n

        small_k = [[] for _ in range(B)]
        large_k = []

        for l, r, k, v in queries:
            if k < B:
                small_k[k].append((l, r, v))
            else:
                large_k.append((l, r, k, v))

        # ✅ optimized small k
        for k in range(1, B):
            if not small_k[k]:
                continue

            for rem in range(k):
                arr = []

                # collect indices for this remainder
                for i in range(rem, n, k):
                    arr.append(i)

                m = len(arr)
                pref = [1] * (m + 1)

                for l, r, v in small_k[k]:
                    if l % k != rem:
                        continue

                    start = (l - rem) // k
                    end = (r - rem) // k

                    pref[start] = (pref[start] * v) % MOD
                    if end + 1 < len(pref):
                        pref[end + 1] = (pref[end + 1] * pow(v, MOD - 2, MOD)) % MOD

                cur = 1
                for i in range(m):
                    cur = (cur * pref[i]) % MOD
                    mul[arr[i]] = (mul[arr[i]] * cur) % MOD

        # large k direct
        for l, r, k, v in large_k:
            for i in range(l, r + 1, k):
                mul[i] = (mul[i] * v) % MOD

        # final XOR
        res = 0
        for i in range(n):
            res ^= (nums[i] * mul[i]) % MOD

        return res