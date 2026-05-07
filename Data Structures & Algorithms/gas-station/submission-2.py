class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        jump = 0
        ret = 0

        for i in range(len(gas)):
            
            jump += gas[i]
            jump -= cost[i]

            if jump < 0:
                jump = 0
                ret = i + 1
        
        if jump < 0:
            return -1
        return ret