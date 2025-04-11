from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):       # Start from the end
            for j in range(i + 1, len(nums)):        # Look ahead
                if nums[i] < nums[j]:                # Valid increasing step
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # Update with max possible subsequence length

        return max(LIS)

# Example Usage
sol = Solution()

# Test Case 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of LIS for {nums1} ->", sol.lengthOfLIS(nums1))  # Output: 4 ([2, 3, 7, 101])

# Test Case 2
nums2 = [0, 1, 0, 3, 2, 3]
print(f"Length of LIS for {nums2} ->", sol.lengthOfLIS(nums2))  # Output: 4 ([0, 1, 2, 3])

# Test Case 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
print(f"Length of LIS for {nums3} ->", sol.lengthOfLIS(nums3))  # Output: 1 (all are equal)

# Test Case 4
nums4 = [4, 10, 4, 3, 8, 9]
print(f"Length of LIS for {nums4} ->", sol.lengthOfLIS(nums4))  # Output: 3 ([4, 8, 9])