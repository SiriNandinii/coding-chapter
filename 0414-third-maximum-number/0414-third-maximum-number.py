class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist=[]
        for i in range(len(nums)):
            if nums[i] not in dist:
                dist.append(nums[i])
        dist.sort(reverse=True)
        if len(dist)<3:
            return dist[0]
        else:
            return dist[2]