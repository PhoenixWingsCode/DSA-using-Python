import sys

def matrix_chain_order(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # l is chain length
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[1][n - 1]

# Example
arr = [10, 100, 5, 50]
print("Minimum number of multiplications is:", matrix_chain_order(arr))