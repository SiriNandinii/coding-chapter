class Solution(object):
    def minMirrorPairDistance(self, nums):
        mp = {}  # reversed value -> latest index
        ans = float('inf')

        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])

            # check if current number matches someone's reverse
            if nums[i] in mp:
                ans = min(ans, i - mp[nums[i]])

            mp[rev] = i  # store reversed number

        return -1 if ans == float('inf') else ans