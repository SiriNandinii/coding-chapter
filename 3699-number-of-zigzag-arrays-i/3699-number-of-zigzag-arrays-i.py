class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        # Length 2 initialization
        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        if n == 2:
            return sum(up[1:]) % MOD

        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for v in range(1, m + 1):
                pref_down[v] = (pref_down[v - 1] + down[v]) % MOD
                pref_up[v] = (pref_up[v - 1] + up[v]) % MOD

            total_up = pref_up[m]

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for v in range(1, m + 1):
                new_up[v] = pref_down[v - 1]
                new_down[v] = (total_up - pref_up[v]) % MOD

            up, down = new_up, new_down

        return (sum(up[1:]) + sum(down[1:])) % MOD