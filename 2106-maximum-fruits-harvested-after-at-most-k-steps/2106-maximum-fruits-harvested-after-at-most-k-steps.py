from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0
        n = len(fruits)
        left = 0
        total = 0

        for right in range(n):
            total += fruits[right][1]

            # While the current window is not reachable within k steps, shrink it from the left
            while left <= right and self.min_steps(fruits, left, right, startPos) > k:
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits

    def min_steps(self, fruits, left, right, startPos):
        leftPos = fruits[left][0]
        rightPos = fruits[right][0]

        # Two options:
        # 1. Go left to leftPos, then to rightPos
        # 2. Go right to rightPos, then to leftPos
        return min(abs(startPos - leftPos) + (rightPos - leftPos),
                   abs(startPos - rightPos) + (rightPos - leftPos))
