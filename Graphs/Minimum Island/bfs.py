from collections import deque

def min_island(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    min_size = float('inf')

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        size = 0

        while queue:
            row, col = queue.popleft()
            size += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    visited[nr][nc] = True

        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                island_size = bfs(r, c)
                min_size = min(min_size, island_size)

    return min_size if min_size != float('inf') else 0

# Example usage:
grid = [
    ['1', '0', '0', '1', '0'],
    ['1', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['0', '0', '0', '1', '1']
]

print(min_island(grid))  # Output: 1
