#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (44.13%)
# Likes:    1059
# Dislikes: 127
# Total Accepted:    103.1K
# Total Submissions: 233.3K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
#
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target == 0:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(min(nums), target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]


class RecursiveSolution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            count += self.combinationSum4(nums, target - num)
        return count


# @lc code=end
