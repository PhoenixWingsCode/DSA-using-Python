def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, idx):
        # If out of bounds or current letter doesn't match, return False
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c]!= word[idx]:
            return False
        
        # If all characters are matched
        if idx == len(word) - 1:
            return True
        
        # Temporarily mark the current cell as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore neighbors in 4 directions: up, down, left, right
        found = (backtrack(r+1, c, idx+1) or
                 backtrack(r-1, c, idx+1) or
                 backtrack(r, c+1, idx+1) or
                 backtrack(r, c-1, idx+1))
        
        # Restore the original value after exploring
        board[r][c] = temp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:  # Optimization: start only at cells matching first letter
                if backtrack(i, j, 0):
                    return True
    return False

# Example usage
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']]

print(exist(board, "ABCCED"))  # Output: True
print(exist(board, "SEE"))     # Output: True
print(exist(board, "ABCB"))    # Output: False