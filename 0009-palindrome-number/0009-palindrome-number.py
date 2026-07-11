class Solution:
    def isPalindrome(self, x: int) -> bool:
        def check(num):
            num = str(num)
            temp = num
            return temp == num[::-1]

        result = check(x)
        MIN, MAX = -2**31, 2**31 - 1

        return result
        