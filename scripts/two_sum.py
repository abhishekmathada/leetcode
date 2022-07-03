from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Takes input nums --> list of integers and target --> integer
            Returns list of indices of two numbers such that they add up to target
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
