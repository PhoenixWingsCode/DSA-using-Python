def min_subarray_len(target, nums):
    start = 0
    curr_sum = 0
    min_length = float('inf')

    for end in range(len(nums)):
        curr_sum += nums[end]

        # Shrink the window as long as the sum is >= target
        while curr_sum >= target:
            min_length = min(min_length, end - start + 1)
            curr_sum -= nums[start]
            start += 1

    if min_length == float('inf'):
        return 0
    else:
        return min_length

# Example usage:
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target, nums))  # Output: 2 (subarray [4,3])