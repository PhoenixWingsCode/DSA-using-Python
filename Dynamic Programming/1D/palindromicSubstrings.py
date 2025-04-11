class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # Count odd-length palindromes
            res += self.countPali(s, i, i)
            # Count even-length palindromes
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

# 🎯 Example Usage
solution = Solution()

# Example 1
s1 = "abc"
print("Input:", s1)
print("Number of Palindromic Substrings:", solution.countSubstrings(s1))  # Output: 3

# Example 2
s2 = "aaa"
print("\nInput:", s2)
print("Number of Palindromic Substrings:", solution.countSubstrings(s2))  # Output: 6

# Example 3
s3 = "abba"
print("\nInput:", s3)
print("Number of Palindromic Substrings:", solution.countSubstrings(s3))  # Output: 6
