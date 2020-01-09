#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.48%)
# Likes:    3531
# Dislikes: 115
# Total Accepted:    415.7K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        previous_1_house, previous_2_houses = 0, 0
        for num in nums:
            previous_1_house, previous_2_houses = max(
                num + previous_2_houses, previous_1_house), previous_1_house
        return previous_1_house


# @lc code=end
class AnotherDPSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        previous_1_house, previous_2_houses = max(nums[0], nums[1]), nums[0]
        for i in range(2, len(nums)):
            previous_1_house, previous_2_houses = max(
                nums[i] + previous_2_houses,
                previous_1_house), previous_1_house
        return max(previous_1_house, previous_2_houses)


class OptimizedDPSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        max_money_3_houses_before, max_money_2_houses_before, max_money_1_house_before = nums[
            0], nums[1], nums[2] + nums[0]
        for i in range(3, len(nums)):
            max_money_1_house_before, max_money_2_houses_before, max_money_3_houses_before = max(
                max_money_2_houses_before, max_money_3_houses_before
            ) + nums[i], max_money_1_house_before, max_money_2_houses_before
        return max(max_money_1_house_before, max_money_2_houses_before)


class DPSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        max_money_before_i = [0] * len(nums)
        max_money_before_i[0], max_money_before_i[1], max_money_before_i[
            2] = nums[0], nums[1], nums[2] + nums[0]
        for i in range(3, len(nums)):
            max_money_before_i[i] = max(max_money_before_i[i - 2],
                                        max_money_before_i[i - 3]) + nums[i]
        return max(max_money_before_i[-1], max_money_before_i[-2])
