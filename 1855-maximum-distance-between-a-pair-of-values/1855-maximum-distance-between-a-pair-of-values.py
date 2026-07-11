class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxi = 0
        j = 0
        i = 0
        while i<len(nums1) and j<len(nums2):

            if nums1[i]<=nums2[j]:
                maxi = max(maxi, (j-i))
                j += 1
            else:
                i+=1

        return maxi        