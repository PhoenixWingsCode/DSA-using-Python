def clear_kth_bit(N, K):
    """
    Clear the K-th bit of the number N
    :param N: The original number
    :param K: The position of the bit to clear (0-indexed)
    :return: The number with the K-th bit cleared
    """
    return N & ~(1 << K)

# Example usage:
N = 5  # Binary representation: 101
K = 1
result = clear_kth_bit(N, K)
print("Original number:", N)         # Output: 5
print("After clearing the", K, "th bit:", result)  # Output: 4, (Binary 100)