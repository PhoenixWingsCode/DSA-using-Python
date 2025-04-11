from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with a large number (amount + 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: zero coins needed to make amount 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])  # Take the minimum coins needed

        return dp[amount] if dp[amount] != amount + 1 else -1

#Example Usage
sol = Solution()

# Test case 1
coins = [1, 2, 5]
amount = 11
print("Coins:", coins)
print("Amount:", amount)
print("Minimum coins needed:", sol.coinChange(coins, amount))  # Output: 3 (5 + 5 + 1)

# Test case 2
coins2 = [2]
amount2 = 3
print("\nCoins:", coins2)
print("Amount:", amount2)
print("Minimum coins needed:", sol.coinChange(coins2, amount2))  # Output: -1 (Not possible)

# Test case 3
coins3 = [1]
amount3 = 0
print("\nCoins:", coins3)
print("Amount:", amount3)
print("Minimum coins needed:", sol.coinChange(coins3, amount3))  # Output: 0