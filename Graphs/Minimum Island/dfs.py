def min_island(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    min_size = float('inf')

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == '0' or (r, c) in visited):
            return 0

        visited.add((r, c))
        size = 1  # current cell

        # Explore all 4 directions
        size += dfs(r + 1, c)
        size += dfs(r - 1, c)
        size += dfs(r, c + 1)
        size += dfs(r, c - 1)

        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                island_size = dfs(r, c)
                if island_size > 0:
                    min_size = min(min_size, island_size)

    return min_size if min_size != float('inf') else 0

# Example usage:
grid = [
    ['1', '0', '0', '1', '0'],
    ['1', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '0']
]

print(min_island(grid))  # Output: 1
