class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        l= 0

        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                time += min(neededTime[l] , neededTime[r])
                if neededTime[l] < neededTime[r]:
                    l = r
            else:
                l = r
        return time