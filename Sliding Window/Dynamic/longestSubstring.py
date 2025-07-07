def length_of_longest_substring(s):
    seen = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            # Move start right after the previous index of s[end]
            start = seen[s[end]] + 1
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

# Example usage:
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3 ("abc")