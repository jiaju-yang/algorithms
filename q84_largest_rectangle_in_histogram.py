#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (32.89%)
# Likes:    2681
# Dislikes: 65
# Total Accepted:    215.9K
# Total Submissions: 651.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#
from typing import List


# @lc code=start
class StackSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area


# @lc code=end
class DPSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_higher_than_i = [0] * len(heights)
        right_higher_than_i = [0] * len(heights)
        max_area = 0
        for i in range(len(heights)):
            left = i - 1
            while left >= 0:
                if heights[left] >= heights[i]:
                    left_higher_than_i[i] += (left_higher_than_i[left] + 1)
                    left = left - left_higher_than_i[left] - 1
                else:
                    break
        for i in range(len(heights) - 1, -1, -1):
            right = i + 1
            while right < len(heights):
                if heights[right] >= heights[i]:
                    right_higher_than_i[i] += (right_higher_than_i[right] + 1)
                    right = right + right_higher_than_i[right] + 1
                else:
                    break
        for i in range(len(heights)):
            current_max_area = (right_higher_than_i[i] +
                                left_higher_than_i[i] + 1) * heights[i]
            max_area = max(max_area, current_max_area)
        return max_area


class BruteForceSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left_higher_than_i, right_higher_than_i = i, i
            for j in range(i - 1, -1, -1):
                if heights[j] >= heights[i]:
                    left_higher_than_i = j
                else:
                    break
            for j in range(i + 1, len(heights)):
                if heights[j] >= heights[i]:
                    right_higher_than_i = j
                else:
                    break
            current_max_area = (right_higher_than_i - left_higher_than_i +
                                1) * heights[i]
            max_area = max(max_area, current_max_area)
        return max_area


Solution = StackSolution
