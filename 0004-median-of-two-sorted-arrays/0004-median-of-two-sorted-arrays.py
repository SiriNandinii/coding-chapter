class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        le = len(nums)

        if le%2==1:
            return float(nums[le//2])

        else:
            return (nums[le//2] + nums[le//2 -1])/2     