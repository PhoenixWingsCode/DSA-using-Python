class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # initialize last row as 1s (only one way to go right)

        for i in range(m - 1):  # iterate from bottom to top
            newRow = [1] * n
            for j in range(n - 2, -1, -1):  # iterate right to left
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# Example usage:
solution = Solution()
m = 3
n = 7
print(f"Number of unique paths in a {m}x{n} grid is:", solution.uniquePaths(m, n))