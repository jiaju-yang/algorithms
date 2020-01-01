#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (30.46%)
# Likes:    2926
# Dislikes: 127
# Total Accepted:    269.7K
# Total Submissions: 883K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        iterator = iter(nums)
        result = min_product = max_product = next(iterator)
        for num in iterator:
            max_product, min_product = max(max_product * num,
                                           min_product * num,
                                           num), min(max_product * num,
                                                     min_product * num, num)
            result = max(result, max_product)
        return result


# @lc code=end
