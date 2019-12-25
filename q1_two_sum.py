#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2 or target is None:
            return []
        checked = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in checked:
                return [checked[complement], i]
            checked[num] = i
        return []


# @lc code=end
