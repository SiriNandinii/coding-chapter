from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Function to get longest alternating parity subsequence
        def max_alternating(start_parity):
            count = 0
            expected = start_parity
            for num in nums:
                if num % 2 == expected:
                    count += 1
                    expected ^= 1  # Toggle between 0 and 1
            return count

        # Case 1: All even or all odd elements (same parity)
        count_same_parity = max(
            sum(1 for num in nums if num % 2 == 0),
            sum(1 for num in nums if num % 2 == 1)
        )

        # Case 2: Alternating parity elements (even-odd-even or odd-even-odd)
        count_alternating = max(
            max_alternating(0),  # Starting with even
            max_alternating(1)   # Starting with odd
        )

        # Return the best of both cases
        return max(count_same_parity, count_alternating)
