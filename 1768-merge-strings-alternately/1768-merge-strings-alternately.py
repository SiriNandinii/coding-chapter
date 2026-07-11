class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if len(word1)>len(word2):
            maxi = word1
            mini = word2
        else:
            maxi = word2
            mini = word1
        result = ""
        
        for i in range(len(mini)):
            result += word1[i] + word2[i]
        
        return result if len(word1) == len(word2) else result+maxi[i+1:]
        