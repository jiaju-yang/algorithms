#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (45.63%)
# Likes:    3118
# Dislikes: 103
# Total Accepted:    539.7K
# Total Submissions: 1.2M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#


# @lc code=start
class SolutionIterativeWithSpaceOptimization:
    def climbStairs(self, n: int) -> int:
        previous_two, previous = 1, 2
        if n == 1:
            return previous_two
        if n == 2:
            return previous
        for _ in range(2, n):
            cur = previous + previous_two
            previous_two, previous = previous, cur
        return cur


class SolutionIterative:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        stairs = [0] * n
        stairs[0], stairs[1] = 1, 2
        for i in range(2, n):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[n - 1]


class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class SolutionRecursiveWithTimeOptimization:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1

        def driver(previous_two, previous, cur):
            if cur < 1:
                return previous
            return driver(previous, previous + previous_two, cur - 1)

        return driver(1, 2, n - 2)


Solution = SolutionRecursiveWithTimeOptimization

# @lc code=end
