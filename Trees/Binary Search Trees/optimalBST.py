def optimal_bst(keys, freq, n):
    # Create an auxiliary 2D matrix to store the cost of subproblems
    cost = [[0 for x in range(n)] for y in range(n)]

    # Cost for a single key is equal to its frequency
    for i in range(n):
        cost[i][i] = freq[i]

    # Now we need to consider chains of length 2, 3, ..., n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            # Try making all keys in interval keys[i..j] as root
            for r in range(i, j + 1):
                # Cost when keys[r] becomes root
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])

                # Update the cost if it's lower than the current cost
                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]

# Example usage
keys = [10, 12, 20]
freq = [34, 8, 50]
n = len(keys)
print("Cost of Optimal BST is", optimal_bst(keys, freq, n))