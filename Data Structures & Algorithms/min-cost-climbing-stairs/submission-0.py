class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 2:
            return min(cost[0], cost[1])
        elif len(cost) == 1:
            return cost[0]
        
        INF = float("inf")
        n = len(cost)
        arr = [INF] * (n + 1)

        arr[0] = 0
        arr[1] = 0

        for i in range(2, n + 1):

            arr[i] = min(arr[i-1] + cost[i-1], arr[i-2] + cost[i-2])
        
        return arr[n]

