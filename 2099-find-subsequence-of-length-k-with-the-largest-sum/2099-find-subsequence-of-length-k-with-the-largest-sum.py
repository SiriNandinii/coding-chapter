class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Get indices of the k largest elements
        indexed_nums = list(enumerate(nums))
        # Sort by value descending, keep k largest
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        # Sort by original index to preserve order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        # Extract the values only
        return [val for idx, val in top_k_sorted]
