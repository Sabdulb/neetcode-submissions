class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        mp = Counter(hand)

        hand.sort()
        for val in hand:

            if mp[val] <= 0:
                continue
            
            for i in range(val, val + groupSize):
                if i not in mp or mp[i] <= 0:
                    return False
                
                mp[i] -= 1
        
        return True