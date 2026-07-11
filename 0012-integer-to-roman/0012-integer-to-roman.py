class Solution:
    def intToRoman(self, num: int) -> str:
        powers_of_10 = 'IXCM'
        powers_of_5 = 'VLD'

        dict_of_10 = {1: 'I', 10: 'X', 100: 'C', 1000: 'M'}
        dict_of_5 = {5: 'V', 50: 'L', 500: 'D'}


        conversions = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = ''
        while num != 0:
            for value,symbol in conversions:
                if num >= value:
                    result += symbol
                    num -= value
                    break

        return result                                             