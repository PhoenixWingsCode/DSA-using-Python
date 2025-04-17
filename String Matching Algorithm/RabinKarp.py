def rabin_karp(text, pattern):
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    n = len(text)
    m = len(pattern)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        if p == t:
            # Check for characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(f"Pattern found at index {i}")

        # Calculate hash value for next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

# Example usage
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
rabin_karp(text, pattern)
