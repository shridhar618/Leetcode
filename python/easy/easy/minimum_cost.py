class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n=len(cost)

        total=0

        for i in range(n):
            if i%3!=2:
                total+=cost[i]
        
        return total
                
                
            
        