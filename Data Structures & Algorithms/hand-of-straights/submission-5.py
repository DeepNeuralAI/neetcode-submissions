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
        
        for num in count:
            heapq.heappush(minHeap, num)
        
        for _ in range(numGroups):
            while minHeap and count[minHeap[0]] == 0:
                heapq.heappop(minHeap)
            
            num = minHeap[0]
            if count[num] - 1 > 0:
                heapq.heappush(minHeap, num)
            
            for i in range(groupSize):
                start = num + i

                if start in count and count[start] > 0:
                    count[start] -= 1
                else:
                    return False
        
        return True



            

            
            
            

            


            

        


        


            
        