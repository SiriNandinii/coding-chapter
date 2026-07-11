class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, len(nums)-1
        nums.sort()
        while left<right:
            sum = nums[left]+nums[right]
            if sum == k:
                left+=1
                right-=1
                res +=1
            elif sum<k:
                left += 1
            else:
                right -= 1
        return res
        
        