class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        temp = 0
        start = 0
        for i in range(len(gas)):
            temp += gas[i] - cost[i]
            if temp < 0:
                temp = 0
                start = i + 1
        
        return start