class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with infinity, except for dp[0] = 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # Build up dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, no combination can make the amount
        return dp[amount] if dp[amount] != float('inf') else -1
