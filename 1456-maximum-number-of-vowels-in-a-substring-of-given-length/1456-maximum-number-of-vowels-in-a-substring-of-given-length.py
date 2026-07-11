class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        sub = s[:k]
        current_sum = 0
        for i in sub:
            if i in vowels:
                current_sum += 1
        maxi = current_sum


        for j in range(k, len(s)):
            
            if s[j-k] in vowels:
                current_sum -= 1
            if s[j] in vowels:
                current_sum += 1
            
            maxi = max(maxi, current_sum)

        return maxi