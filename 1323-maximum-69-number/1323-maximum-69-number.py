class Solution:
    def maximum69Number (self, num: int) -> int:
        maximum = num
        num = list(map(int,str(num)))
        for index, digit in enumerate(num):
            if digit == 6:
                num[index] = 9
                temp = int("".join(map(str, num)))
                if temp > maximum:
                    maximum = temp
                    break
        return maximum
