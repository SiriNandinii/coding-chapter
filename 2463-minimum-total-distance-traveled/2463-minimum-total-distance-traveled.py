class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        from functools import lru_cache

        n = len(robot)
        m = len(factory)

        @lru_cache(None)
        def dp(i, j):
            # all robots assigned
            if i == n:
                return 0

            # no factories left
            if j == m:
                return float('inf')

            # OPTION 1: skip this factory
            res = dp(i, j+1)

            pos, limit = factory[j]

            cost = 0
            # OPTION 2: assign k robots to this factory
            for k in range(limit):
                if i + k >= n:
                    break

                cost += abs(robot[i+k] - pos)
                res = min(res, cost + dp(i+k+1, j+1))

            return res

        return dp(0, 0)