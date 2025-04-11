class Solution:
    # Iterative Dynamic Programming Solution
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # Base case: one way to decode empty string

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]

    # Recursive + Memoization (DFS)
    def numDecodingsDFS(self, s: str) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)
    
# Create instance
sol = Solution()

# Example 1
s1 = "226"
print("Input:", s1)
print("Ways to Decode (Iterative):", sol.numDecodings(s1))
print("Ways to Decode (Recursive):", sol.numDecodingsDFS(s1))

# Example 2
s2 = "06"
print("\nInput:", s2)
print("Ways to Decode (Iterative):", sol.numDecodings(s2))
print("Ways to Decode (Recursive):", sol.numDecodingsDFS(s2))

# Example 3
s3 = "12"
print("\nInput:", s3)
print("Ways to Decode (Iterative):", sol.numDecodings(s3))
print("Ways to Decode (Recursive):", sol.numDecodingsDFS(s3))