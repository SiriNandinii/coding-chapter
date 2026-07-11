from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        lo = float('inf')
        hi = 0

        for _, y, l in squares:
            total += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)

        target = total / 2

        def area_below(line):
            area = 0.0
            for _, y, l in squares:
                if line <= y:
                    continue
                elif line >= y + l:
                    area += l * l
                else:
                    area += l * (line - y)
            return area

        for _ in range(60):
            mid = (lo + hi) / 2

            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid

        return hi