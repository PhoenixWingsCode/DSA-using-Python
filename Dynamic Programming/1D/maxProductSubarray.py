from typing import List

class Solution:
    def maxProductSubarray(self, nums: List[int]) -> int:
        res = max(nums)  # Start with the maximum number in the array
        curMin, curMax = 1, 1  # Initialize current min and max products

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1  # Reset when zero is encountered
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)  # Update result
        return res

# Example Usage
sol = Solution()

# Test Case 1
nums1 = [2, 3, -2, 4]
print("Array:", nums1)
print("Maximum Product Subarray:", sol.maxProductSubarray(nums1))  # Output: 6 (2 * 3)

# Test Case 2
nums2 = [-2, 0, -1]
print("\nArray:", nums2)
print("Maximum Product Subarray:", sol.maxProductSubarray(nums2))  # Output: 0

# Test Case 3
nums3 = [2, -5, -2, -4, 3]
print("\nArray:", nums3)
print("Maximum Product Subarray:", sol.maxProductSubarray(nums3))  # Output: 240

# Test Case 4
nums4 = [0, -3, 1, -2]
print("\nArray:", nums4)
print("Maximum Product Subarray:", sol.maxProductSubarray(nums4))  # Output: 6