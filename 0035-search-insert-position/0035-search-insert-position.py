class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        key = 0
        for i in range(len(nums)+1):
            if i==len(nums):
                return i
            elif nums[i]>=target:
                return i
            else:
                continue           