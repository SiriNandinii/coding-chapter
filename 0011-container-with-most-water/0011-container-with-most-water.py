class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        mv = 0
        
        while left<right:
            h = min(height[left], height[right])
            w = right - left
            v = w*h
            mv = max(mv, v)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return mv