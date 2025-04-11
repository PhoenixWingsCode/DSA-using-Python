class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

# Example Usage
solution = Solution()

# Example 1
s1 = "babad"
print("Input:", s1)
print("Longest Palindromic Substring:", solution.longestPalindrome(s1))

# Example 2
s2 = "cbbd"
print("\nInput:", s2)
print("Longest Palindromic Substring:", solution.longestPalindrome(s2))

# Example 3
s3 = "a"
print("\nInput:", s3)
print("Longest Palindromic Substring:", solution.longestPalindrome(s3))

# Example 4
s4 = "forgeeksskeegfor"
print("\nInput:", s4)
print("Longest Palindromic Substring:", solution.longestPalindrome(s4))