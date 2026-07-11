class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        first = [i for i in first]
        second = "asdfghjkl"
        second = [i for i in second]
        third = "zxcvbnm"
        third = [i for i in third]

        ans = []

        def finding(word):
            w = [i.lower() for i in word]
            if all(ch in first for ch in w):
                ans.append(word)
            elif all(ch in second for ch in w):
                ans.append(word)
            elif all(ch in third for ch in w):
                ans.append(word)
            else:
                pass
        
        for word in words:
            finding(word)
        
        return ans