from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Memoization dictionary to store results of subproblems
        dp = {}  # key = (i, buying), value = max profit from that state

        def dfs(i, buying):
            # Base case: If we reach the end of the list, no more transactions possible
            if i >= len(prices):
                return 0

            # If already calculated, return from memo
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Cooldown: skip today and keep state
            cooldown = dfs(i + 1, buying)

            if buying:
                # Option 1: Buy today (-prices[i]), move to next day in "selling" state
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Option 1: Sell today (+prices[i]), skip 1 day, move to buying state
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]

        # Start at day 0 with the option to buy
        return dfs(0, True)

# Example usage
solution = Solution()
prices = [1, 2, 3, 0, 2]
print("Maximum Profit:", solution.maxProfit(prices))