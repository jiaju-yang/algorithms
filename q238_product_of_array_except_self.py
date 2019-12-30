#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (57.70%)
# Likes:    3266
# Dislikes: 278
# Total Accepted:    356.3K
# Total Submissions: 615.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums) - 1):
            result[i + 1] = result[i] * nums[i]
        previous_right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= previous_right_product
            previous_right_product *= nums[i]
        return result


class LeftAndRightProductListsSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        left[0] = 1
        for i in range(len(nums) - 1):
            left[i + 1] = (left[i] * nums[i])
        right = [0] * len(nums)
        right[-1] = 1
        for i in range(len(nums) - 1, 0, -1):
            right[i - 1] = (right[i] * nums[i])
        return [left[i] * right[i] for i in range(len(nums))]


# @lc code=end
