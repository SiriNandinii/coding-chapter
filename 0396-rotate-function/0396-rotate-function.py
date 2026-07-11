class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        # F(0)
        curr = sum(i * nums[i] for i in range(n))

        ans = curr

        # Relation:
        # F(k) = F(k-1) + total - n * nums[n-k]
        for k in range(1, n):
            curr = curr + total - n * nums[n - k]
            ans = max(ans, curr)

        return ans