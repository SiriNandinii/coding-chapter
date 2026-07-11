class Solution:
    def reverse(self, x: int) -> int:
        def reversing(num):
            return num[::-1]
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        x = str(x)

        if x.startswith('-'):
            rev = int('-' + reversing(x[1:]))
        else:
            rev = int(reversing(x))

        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
