class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        from functools import lru_cache

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1):
                # Returns:
                # (number of valid numbers, total waviness)

                if pos == len(digits):
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    # Still dealing with leading zeros
                    if not started and d == 0:
                        count, waviness = dp(
                            pos + 1,
                            new_tight,
                            False,
                            -1,
                            -1
                        )

                    else:
                        if not started:
                            # First actual digit
                            new_prev2 = -1
                            new_prev1 = d
                            extra = 0

                        elif prev2 == -1:
                            # We have exactly one previous digit
                            new_prev2 = prev1
                            new_prev1 = d
                            extra = 0

                        else:
                            # We now have three digits:
                            # prev2, prev1, d
                            new_prev2 = prev1
                            new_prev1 = d

                            if (prev1 > prev2 and prev1 > d) or \
                               (prev1 < prev2 and prev1 < d):
                                extra = 1
                            else:
                                extra = 0

                        count, waviness = dp(
                            pos + 1,
                            new_tight,
                            True,
                            new_prev2,
                            new_prev1
                        )

                        total_waviness += waviness + extra * count
                        total_count += count

                        continue

                    total_waviness += waviness
                    total_count += count

                return total_count, total_waviness

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)