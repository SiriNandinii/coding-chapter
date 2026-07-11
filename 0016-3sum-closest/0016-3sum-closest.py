class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to enable two-pointer technique
        n = len(nums)
        closest_sum = float('inf')
        min_diff = float('inf')
        
        for i in range(n - 2):  # Fix the first element
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)
                
                # Update closest_sum if current_sum is closer to target
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                
                # Move pointers to get closer to the target
                if current_sum < target:
                    left += 1  # Need a larger sum
                elif current_sum > target:
                    right -= 1  # Need a smaller sum
                else:
                    return target  # Exact match found
                    
        return closest_sum