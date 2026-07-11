class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i,v in enumerate(flowerbed):
            left = (i==0) or (flowerbed[i-1]==0)
            right = (i == len(flowerbed)-1) or (flowerbed[i+1]==0)

            if left and right and n>0 and v==0:
                flowerbed[i] = 1
                n -= 1
            
        
        if n==0:
            return True
        return False