from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:

        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)

        def dist(a, b):
            if a is None or b is None:
                return 0
            x1, y1 = get_pos(a)
            x2, y2 = get_pos(b)
            return abs(x1 - x2) + abs(y1 - y2)

        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0

            # Option 1: use finger1
            use_f1 = dist(f1, word[i]) + dp(i+1, word[i], f2)

            # Option 2: use finger2
            use_f2 = dist(f2, word[i]) + dp(i+1, f1, word[i])

            return min(use_f1, use_f2)

        return dp(0, None, None)