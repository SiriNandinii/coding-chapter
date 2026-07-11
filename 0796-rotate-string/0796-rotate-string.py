class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            s.append(s[0])
            s = s[1:]
            if "".join(s)==goal:
                return True
        return False
        