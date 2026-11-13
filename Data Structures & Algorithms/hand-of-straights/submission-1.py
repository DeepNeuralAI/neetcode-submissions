class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        count = defaultdict(int)
        numGroups = len(hand) // groupSize
        
        for num in hand:
            count[num] += 1
        
        idx = 0
       
        for _ in range(numGroups):
            
            while count[hand[idx]] < 1:
                idx += 1

            start = hand[idx]
            
            for i in range(groupSize):
                num = i + start
                if num in count and count[num] > 0:
                    count[num] -= 1
                else:
                    return False
            
            idx += 1
        
        return True
                
        


            
        