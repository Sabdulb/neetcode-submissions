class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        mp = Counter(hand)

        for i in range(len(hand)):

            if mp[hand[i]] <= 0:
                continue
            
            cur = hand[i]

            while cur - 1 in mp and mp[cur-1] > 0:
                cur = cur - 1
            
            for val in range(cur, cur + groupSize):
                if val in mp and mp[val] > 0:
                    mp[val] -= 1
                else:
                    return False
        
        return True