#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.91%)
# Likes:    2828
# Dislikes: 256
# Total Accepted:    345K
# Total Submissions: 1M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
from typing import List


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        most_close_position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= most_close_position:
                most_close_position = i
        return most_close_position == 0


# @lc code=end


class BottomUpDPSolution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        can_be_reached = [False] * len(nums)
        can_be_reached[0] = True
        max_jump = max(nums)
        for i in range(1, len(nums)):
            for j in range(i - max_jump, i):
                if i - j <= nums[j] and can_be_reached[j]:
                    can_be_reached[i] = True
                    break
        return can_be_reached[-1]
