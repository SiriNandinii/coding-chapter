class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        shortest = strs[0]

        for i in range(len(shortest)):
            for word in strs:
                if word[i]!=shortest[i]:
                    return shortest[:i]
        return shortest       