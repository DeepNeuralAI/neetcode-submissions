import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = defaultdict(int)
        numGroups = len(hand) // groupSize
        minHeap = []
        
        for num in hand:
            count[num] += 1
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        
        while minHeap:
            first = minHeap[0]

            for i in range(groupSize):
                start = first + i

                if start not in count or count[start] == 0:
                    return False
                
                count[start] -= 1

                if count[start] == 0 and minHeap[0] == start:
                    heapq.heappop(minHeap)

        return True



            

            
            
            

            


            

        


        


            
        