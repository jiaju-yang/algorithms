#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.44%)
# Likes:    3441
# Dislikes: 387
# Total Accepted:    539.9K
# Total Submissions: 1.6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
#
from typing import List


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1  # 如果right=len(nums)有可能造成比较的时候位置溢出数组
        while left <= right:  # 如果是<会漏掉长度为1的数组
            mid = (left + right) >> 1
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:  # 数组长度为2的时候left=mid
                if nums[left] <= target < nums[mid]:  # target有可能等于left位置的数
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# @lc code=end
