from typing import List

class Solution:
    def minCostCS(self, cost: List[int]) -> int:
        cost.append(0)  # Add 0 to represent the top of the stairs

        # Start from the third last step and move backwards
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])  # Add min cost from next 2 steps

        return min(cost[0], cost[1])  # Start from step 0 or step 1
    
cost = [10, 15, 20]  # Cost to step on each stair
solution = Solution()
result = solution.minCostCS(cost)
print("Minimum cost to reach the top:", result)