def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        # Swap characters at left and right pointers
        chars[left], chars[right] = chars[right], chars[left]
        # Move pointers closer
        left += 1
        right -= 1

    return ''.join(chars)

# Test
print(reverse_string("converging"))  # Output: gnigrevnoc