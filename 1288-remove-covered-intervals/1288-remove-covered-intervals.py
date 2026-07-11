class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]):

        intervals.sort(key=lambda x: (x[0], -x[1]))

        maxEnd = -1
        ans = 0

        for start, end in intervals:

            if end > maxEnd:
                ans += 1
                maxEnd = end

        return ans