from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string is always segmentable

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if the substring from i matches the word
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break  # No need to check more words

        return dp[0]  # Can the whole string be segmented?

# Example Usage
sol = Solution()

# Test Case 1
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(f"Can '{s1}' be segmented? ->", sol.wordBreak(s1, wordDict1))  # Output: True

# Test Case 2
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print(f"Can '{s2}' be segmented? ->", sol.wordBreak(s2, wordDict2))  # Output: True

# Test Case 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(f"Can '{s3}' be segmented? ->", sol.wordBreak(s3, wordDict3))  # Output: False

# Test Case 4
s4 = "cars"
wordDict4 = ["car", "ca", "rs"]
print(f"Can '{s4}' be segmented? ->", sol.wordBreak(s4, wordDict4))  # Output: True