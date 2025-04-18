def subset_sums(arr):
    def subset_sums_recursive(arr, n, subset_sum, all_sums):
        if n == 0:
            all_sums.append(subset_sum)
            return
        subset_sums_recursive(arr, n-1, subset_sum + arr[n-1], all_sums)
        subset_sums_recursive(arr, n-1, subset_sum, all_sums)

    all_sums = []
    subset_sums_recursive(arr, len(arr), 0, all_sums)
    return all_sums

# Example usage:
arr = [1, 2, 3]
print(subset_sums(arr))  # Output: [6, 5, 4, 3, 3, 2, 1, 0]