#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.34%)
# Likes:    5184
# Dislikes: 630
# Total Accepted:    734.4K
# Total Submissions: 2.9M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            start, end = i + 1, len(nums) - 1
            left, right = start, end
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    if left > start and right < end and nums[left] == nums[
                            left - 1] and nums[right] == nums[right + 1]:
                        pass
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result


class BasedOnTwoSumSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            previous_two_sum = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in previous_two_sum:
                    result.add((nums[i], complement, nums[j]))
                previous_two_sum.add(nums[j])
        return sorted(map(list, result))


# @lc code=end
