from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]  # Edge case: only one house
        return max(
            nums[0],
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

#Example Usage
nums = [2, 3, 2]  # Money in circular houses
solution = Solution()
result = solution.rob(nums)
print("Maximum money that can be robbed:", result)