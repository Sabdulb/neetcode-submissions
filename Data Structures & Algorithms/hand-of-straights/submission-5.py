class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        mp = Counter(hand)

        for i in range(len(hand)):

            c = hand[i]

            if mp[c] == 0:
                continue
            
            while c - 1 in mp and mp[c-1] != 0:
                c = c-1
            
            for j in range(c, c + groupSize):
                if j not in mp or mp[j] == 0:
                    return False
                mp[j] -= 1
        
        return True

