#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.93%)
# Likes:    1441
# Dislikes: 193
# Total Accepted:    355.6K
# Total Submissions: 808.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#
from typing import List

[3, 4, 5, 6, 7, 1, 2]


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) < 2:
            return nums[0]
        left, right = 0, len(nums) - 1

        # No ratation
        if nums[right] > nums[left]:
            return nums[left]

        target = 0
        while nums[target] < nums[target + 1]:
            target = (left + right) >> 1
            if nums[target] < nums[0]:
                right = target
            else:
                left = target
        return nums[target + 1]


# @lc code=end
