from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        # Step 1: store indices of each value
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            # If only one occurrence → no answer
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            # Step 2: binary search
            i = bisect.bisect_left(indices, q)
            
            # neighbors (circular)
            prev_idx = indices[i - 1] if i > 0 else indices[-1]
            next_idx = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            # Step 3: circular distance
            dist1 = abs(q - prev_idx)
            dist2 = abs(q - next_idx)
            
            # circular adjustment
            dist1 = min(dist1, n - dist1)
            dist2 = min(dist2, n - dist2)
            
            ans.append(min(dist1, dist2))
        
        return ans