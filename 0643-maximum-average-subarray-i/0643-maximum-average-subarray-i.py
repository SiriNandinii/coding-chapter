class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        maxi = s

        for i in range(k, len(nums)):
            s = s - nums[i-k] + nums[i]
            maxi = max(maxi, s)
        
        return maxi/k