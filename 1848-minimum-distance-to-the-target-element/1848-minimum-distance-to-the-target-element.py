class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini = float(inf)
        for i in range(len(nums)):
            if nums[i]==target:
                mini = min(mini,abs(start-i))
        return mini
