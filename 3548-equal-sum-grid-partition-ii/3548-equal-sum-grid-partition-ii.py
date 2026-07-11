from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        # ---------- HORIZONTAL ----------
        top_sum = 0
        bottom_sum = total

        top_counter = Counter()
        bottom_counter = Counter()

        for row in grid:
            for val in row:
                bottom_counter[val] += 1

        for i in range(m - 1):
            for val in grid[i]:
                top_sum += val
                bottom_sum -= val

                top_counter[val] += 1
                bottom_counter[val] -= 1
                if bottom_counter[val] == 0:
                    del bottom_counter[val]

            diff = abs(top_sum - bottom_sum)

            if top_sum == bottom_sum:
                return True

            # remove from top
            if top_sum > bottom_sum:
                if diff in top_counter:
                    h, w = i + 1, n
                    if h == 1:
                        if grid[0][0] == diff or grid[0][-1] == diff:
                            return True
                    elif w == 1:
                        if grid[0][0] == diff or grid[i][0] == diff:
                            return True
                    else:
                        return True

            # remove from bottom
            else:
                if diff in bottom_counter:
                    h, w = m - (i + 1), n
                    if h == 1:
                        row = grid[i + 1]
                        if row[0] == diff or row[-1] == diff:
                            return True
                    elif w == 1:
                        if grid[i + 1][0] == diff or grid[m - 1][0] == diff:
                            return True
                    else:
                        return True

        # ---------- VERTICAL ----------
        left_sum = 0
        right_sum = total

        left_counter = Counter()
        right_counter = Counter()

        for row in grid:
            for val in row:
                right_counter[val] += 1

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_sum += val
                right_sum -= val

                left_counter[val] += 1
                right_counter[val] -= 1
                if right_counter[val] == 0:
                    del right_counter[val]

            diff = abs(left_sum - right_sum)

            if left_sum == right_sum:
                return True

            # remove from left
            if left_sum > right_sum:
                if diff in left_counter:
                    h, w = m, j + 1
                    if w == 1:
                        if grid[0][0] == diff or grid[m - 1][0] == diff:
                            return True
                    elif h == 1:
                        if grid[0][0] == diff or grid[0][j] == diff:
                            return True
                    else:
                        return True

            # remove from right
            else:
                if diff in right_counter:
                    h, w = m, n - (j + 1)
                    if w == 1:
                        if grid[0][j + 1] == diff or grid[m - 1][j + 1] == diff:
                            return True
                    elif h == 1:
                        if grid[0][j + 1] == diff or grid[0][n - 1] == diff:
                            return True
                    else:
                        return True

        return False