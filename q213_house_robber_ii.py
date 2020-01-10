#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.75%)
# Likes:    1243
# Dislikes: 42
# Total Accepted:    143.3K
# Total Submissions: 400.1K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_consecutive(nums[:-1]),
                   self.rob_consecutive(nums[1:]))

    def rob_consecutive(self, nums: List[int]) -> int:
        max_previous_1, max_previous_2 = 0, 0
        for num in nums:
            max_previous_1, max_previous_2 = max(
                max_previous_2 + num, max_previous_1), max_previous_1
        return max_previous_1


# @lc code=end
class TwoCasesDPSolution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_consecutive(nums, 0,
                                        len(nums) - 1),
                   self.rob_consecutive(nums, 1, len(nums)))

    def rob_consecutive(self, nums: List[int], start: int, end: int) -> int:
        max_previous_1, max_previous_2 = 0, 0
        for i in range(start, end):
            max_previous_1, max_previous_2 = max(
                max_previous_2 + nums[i], max_previous_1), max_previous_1
        return max_previous_1
