from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for p in set(permutations(str(n))):
            if p[0] != '0':  
                num = int("".join(p))
                # Check if num is a power of 2
                if (num & (num - 1)) == 0:  # bit trick for powers of 2
                    return True
        return False
