class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        max_string = 0
        for i in range(len(s)):
            possible = ''

            for j in range(i, len(s)):                
                if s[j] not in possible:
                    possible += s[j]
                else:
                    break
            max_string = max( max_string, len(possible))
        return max_string