class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if i%3!=2:
                res += cost[i]
        return res

        