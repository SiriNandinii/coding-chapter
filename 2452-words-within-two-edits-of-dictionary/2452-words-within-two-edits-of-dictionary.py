from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def is_within_two_edits(q, d):
            diff = 0
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True
        
        result = []
        
        for q in queries:
            for d in dictionary:
                if is_within_two_edits(q, d):
                    result.append(q)
                    break  # no need to check further
        
        return result