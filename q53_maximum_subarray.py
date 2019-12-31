#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.20%)
# Likes:    5842
# Dislikes: 245
# Total Accepted:    722.7K
# Total Submissions: 1.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        iterator = iter(nums)
        max_sum_so_far = cur_sub_sum = next(iterator)
        for num in iterator:
            cur_sub_sum = num + cur_sub_sum if cur_sub_sum > 0 else num
            max_sum_so_far = max(cur_sub_sum, max_sum_so_far)
        return max_sum_so_far


# @lc code=end
