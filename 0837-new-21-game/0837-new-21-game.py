class Solution:
    def new21Game(self,n: int, k: int, maxPts: int) -> float:
        # Special case: if k == 0, Alice never draws → ends with 0
        # Or if n >= k - 1 + maxPts, Alice cannot exceed n
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)   # dp[i] = probability of getting exactly i points
        dp[0] = 1.0
        windowSum = 1.0  # running sum of last maxPts dp values
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts   # probability to reach i
            if i < k:
                windowSum += dp[i]       # i < k → keep adding to future possibilities
            else:
                result += dp[i]          # i >= k → terminal state
            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]  # maintain sliding window

        return result
