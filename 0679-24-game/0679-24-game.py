from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        
        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = nums[i], nums[j]
                    # Possible next numbers after using a and b
                    candidates = [a+b, a-b, b-a, a*b]
                    if abs(b) > EPSILON:  # avoid divide by zero
                        candidates.append(a/b)
                    if abs(a) > EPSILON:
                        candidates.append(b/a)
                    
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    
                    for c in candidates:
                        if backtrack(next_nums + [c]):
                            return True
            return False
        
        return backtrack([float(x) for x in cards])
