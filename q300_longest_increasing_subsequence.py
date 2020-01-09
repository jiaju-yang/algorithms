#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.72%)
# Likes:    3444
# Dislikes: 77
# Total Accepted:    297.3K
# Total Submissions: 711.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
#
from typing import List


# @lc code=start
class DPBinarySearchSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            index = self.binary_search(dp, nums[i])
            if nums[i] < dp[index]:  # 去掉这行居然时间还耗得多一些，可能是替换操作比判断操作的更费时间
                dp[index] = nums[i]
        return len(dp)

    def binary_search(self, arr, target) -> int:
        """Special binary search method, returns index of the target if it is
        contained; else returns the insertion point.

        """
        start, end = 0, len(arr) - 1
        while end >= start:
            mid = (end + start) >> 1
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start


class DPSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_array_upto_i = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_array_upto_i[i] = max(longest_array_upto_i[j] + 1,
                                                  longest_array_upto_i[i])
        return max(longest_array_upto_i)


Solution = DPBinarySearchSolution
# @lc code=end
