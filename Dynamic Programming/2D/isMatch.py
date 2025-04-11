class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-Down Memoization
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)


# Example usage
solution = Solution()

# Test case 1
s = "aab"
p = "c*a*b"
print(f"Is '{s}' a match for pattern '{p}'? ->", solution.isMatch(s, p))  # Output: True

# Test case 2
s2 = "mississippi"
p2 = "mis*is*p*."
print(f"Is '{s2}' a match for pattern '{p2}'? ->", solution.isMatch(s2, p2))  # Output: False

# Test case 3
s3 = "ab"
p3 = ".*"
print(f"Is '{s3}' a match for pattern '{p3}'? ->", solution.isMatch(s3, p3))  # Output: True