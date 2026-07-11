class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0
            
        n = list(str(n))
        total_sum = 0
        x = ""

        for i in n:
            if int(i)!= 0:
                total_sum += int(i)
                x += i
        
        result = int(x) * total_sum

        return result