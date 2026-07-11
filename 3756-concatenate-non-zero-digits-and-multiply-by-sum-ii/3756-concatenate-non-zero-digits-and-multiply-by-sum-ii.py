from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated value
        pref_num = [0] * (m + 1)
        for i in range(m):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD

        # prefix digit sums
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            x = (pref_num[right] - pref_num[left] * pow10[length]) % MOD
            digit_sum = pref_sum[right] - pref_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans