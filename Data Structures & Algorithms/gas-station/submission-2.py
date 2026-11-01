class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        n = len(gas)

        if total_cost > total_gas:
            return -1
        
        current = 0
        res = 0
        for start in range(n):
            current += gas[start] - cost[start]

            if current < 0:
                current = 0
                res = start + 1
        
        return res


                


                


