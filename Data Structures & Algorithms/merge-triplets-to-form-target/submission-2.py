class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found1, found2, found3, switch1, switch2, switch3 = False, False, False, False, False, False
        c1,c2,c3 = 0,0,0

        if len(triplets) == 0:
            return True
        if len(triplets) == 1:
            switch1, switch2, switch3 = True, True, True
            

        for i in range(len(triplets)):
            if triplets[i][0] == target[0]:
                if triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                    switch1 = True
                found1 = True
            if triplets[i][1] == target[1]:
                if triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                    switch2 = True
                found2 = True
            if triplets[i][2] == target[2]:
                if triplets[i][0] <= target[0] and triplets[i][1] <= target[1]:
                    switch3 = True
                found3 = True
        
        return found1 and found2 and found3 and switch1 and switch2 and switch3