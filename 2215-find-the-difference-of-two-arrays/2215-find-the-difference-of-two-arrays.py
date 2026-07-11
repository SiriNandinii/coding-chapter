class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2 = set(nums1), set(nums2)
        
        a = list(nums1 - nums2)
        b = list(nums2 - nums1)
        return [a,b]
        
        