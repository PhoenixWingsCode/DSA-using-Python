def knapsack(weights, values, capacity):
    n = len(weights)
    memo = {}

    def dfs(i, remaining_capacity):
        if i == n or remaining_capacity == 0:
            return 0
        
        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]

        # Option 1: Don't include current item
        not_take = dfs(i + 1, remaining_capacity)

        # Option 2: Include current item (if it fits)
        take = 0
        if weights[i] <= remaining_capacity:
            take = values[i] + dfs(i + 1, remaining_capacity - weights[i])
        
        memo[(i, remaining_capacity)] = max(take, not_take)
        return memo[(i, remaining_capacity)]

    return dfs(0, capacity)

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print(knapsack(weights, values, capacity))  # Output: 9