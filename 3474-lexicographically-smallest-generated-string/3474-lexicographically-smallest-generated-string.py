class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        size = n + m - 1
        
        word = ['?'] * size
        locked = [False] * size  # NEW
        
        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if word[idx] == '?' or word[idx] == str2[j]:
                        word[idx] = str2[j]
                        locked[idx] = True  # lock it
                    else:
                        return ""
        
        # Step 2: Fill with 'a'
        for i in range(size):
            if word[i] == '?':
                word[i] = 'a'
        
        # Step 3: Fix 'F'
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    changed = False
                    
                    # try to break WITHOUT touching locked
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        
                        if locked[idx]:
                            continue
                        
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != str2[j]:
                                word[idx] = c
                                changed = True
                                break
                        
                        if changed:
                            break
                    
                    if not changed:
                        return ""
        
        return "".join(word)