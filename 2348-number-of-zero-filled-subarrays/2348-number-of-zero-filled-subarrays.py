class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if n == 0:
                count += 1      # extend zero streak
                res += count    # add all subarrays ending here
            else:
                count = 0       # reset streak
        return res
