from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],     # delete
                        cache[i][j + 1],     # insert
                        cache[i + 1][j + 1]  # replace
                    )

        return cache[0][0]

# Example usage
word1 = "horse"
word2 = "ros"
solution = Solution()
result = solution.minDistance(word1, word2)
print(f"Minimum edit distance between '{word1}' and '{word2}' is:", result)