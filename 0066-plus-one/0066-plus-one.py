class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(str(d) for d in digits))+1
        x = str(x)
        y = [int(k) for k in x]
        return y
        