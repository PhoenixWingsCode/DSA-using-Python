def generate_subsets(nums):
    n = len(nums)
    subsets = []
    
    # Total number of subsets is 2^n
    for i in range(1 << n):  # 1 << n is equivalent to 2^n
        subset = []
        for j in range(n):
            # Check if the j-th bit in i is set
            if i & (1 << j):
                subset.append(nums[j])
        subsets.append(subset)
    
    return subsets

# Example usage
nums = [1, 2, 3]
result = generate_subsets(nums)
print("All subsets:", result)
