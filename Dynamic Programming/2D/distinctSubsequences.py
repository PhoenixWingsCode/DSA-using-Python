from typing import Dict, Tuple

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                # Option to use s[i] or skip it
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # Skip s[i]
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)

# Example usage
s = "babgbag"
t = "bag"
solution = Solution()
result = solution.numDistinct(s, t)
print(f"Number of distinct subsequences of '{s}' that match '{t}':", result)