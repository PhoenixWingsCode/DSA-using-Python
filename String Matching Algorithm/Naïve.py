def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        match_found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            matches.append(i)
    
    return matches

# Example usage
text = "abracadabra"
pattern = "abra"
result = naive_string_matching(text, pattern)
print("Pattern found at positions:", result)