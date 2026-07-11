class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                finish1 = max(
                    landStartTime[i] + landDuration[i],
                    waterStartTime[j]
                ) + waterDuration[j]

                # Water -> Land
                finish2 = max(
                    waterStartTime[j] + waterDuration[j],
                    landStartTime[i]
                ) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans