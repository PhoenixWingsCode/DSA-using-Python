from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False  # If total sum is odd, can't partition into equal halves
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
            
        return target in dp

# Example Usage
sol = Solution()

# Example 1
nums1 = [1, 5, 11, 5]
print(f"Can partition {nums1}? ->", sol.canPartition(nums1))  # Output: True (Subset: [1, 5, 5] and [11])

# Example 2
nums2 = [1, 2, 3, 5]
print(f"Can partition {nums2}? ->", sol.canPartition(nums2))  # Output: False

# Example 3
nums3 = [2, 2, 3, 5]
print(f"Can partition {nums3}? ->", sol.canPartition(nums3))  # Output: False

# Example 4
nums4 = [3, 3, 3, 4, 5]
print(f"Can partition {nums4}? ->", sol.canPartition(nums4))  # Output: True ([3, 3, 5] and [3, 4])

# Example 5
nums5 = [1, 2, 5]
print(f"Can partition {nums5}? ->", sol.canPartition(nums5))  # Output: False