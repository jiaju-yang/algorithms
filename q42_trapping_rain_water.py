#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (45.95%)
# Likes:    5296
# Dislikes: 103
# Total Accepted:    407K
# Total Submissions: 879.7K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
#
from typing import List


# @lc code=start
class OptimizedTwoPointersSolution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        total_trap = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                total_trap += max(left_max - height[left], 0)
                left += 1
            else:
                total_trap += max(right_max - height[right], 0)
                right -= 1
        return total_trap


# @lc code=end


class StackSolution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_trap = 0
        for i in range(len(height)):
            while (len(stack) > 0 and height[stack[-1]] < height[i]):
                ground = stack.pop()
                if len(stack) == 0: break
                left = stack[-1]
                right_height = height[i]
                left_height = height[left]
                ground_height = height[ground]
                total_trap += (min(left_height, right_height) -
                               ground_height) * (i - left - 1)
            stack.append(i)
        return total_trap


class TwoPointersSolution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_height_index = height.index(max(height))
        total_trap, max_height_left, max_height_right = 0, 0, 0
        for i in range(max_height_index):
            if max_height_left > height[i]:
                total_trap += max_height_left - height[i]
            else:
                max_height_left = height[i]
        for i in range(len(height) - 1, max_height_index, -1):
            if max_height_right > height[i]:
                total_trap += max_height_right - height[i]
            else:
                max_height_right = height[i]
        return total_trap


class BruteForceSolution:
    def trap(self, height: List[int]) -> int:
        total_trap = 0
        for i in range(1, len(height) - 1):
            max_left, max_right = 0, 0
            for left in range(i):
                max_left = max(max_left, height[left])
            for right in range(i + 1, len(height)):
                max_right = max(max_right, height[right])
            total_trap += max(min(max_left, max_right) - height[i], 0)
        return total_trap


Solution = OptimizedTwoPointersSolution
