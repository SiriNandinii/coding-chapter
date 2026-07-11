class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        level = 0
        maxi = level

        for i in gain:
            level += i
            maxi = max(maxi, level)

        return maxi   
        