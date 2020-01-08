#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (32.75%)
# Likes:    2753
# Dislikes: 93
# Total Accepted:    293.3K
# Total Submissions: 887.3K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
from typing import List


# @lc code=start
class TopDownRecursiveSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        few_coins = [-2] * (amount + 1)
        few_coins[0] = 0

        def driver(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if few_coins[remain] > -2:
                return few_coins[remain]
            few_coins[remain] = -1
            for denomination in coins:
                last_amount = remain - denomination
                previous_min_count = driver(last_amount)
                if previous_min_count < 0:
                    continue
                if few_coins[remain] > -1:
                    few_coins[remain] = min(previous_min_count + 1,
                                            few_coins[remain])
                else:
                    few_coins[remain] = previous_min_count + 1
            return few_coins[remain]

        driver(amount)
        return few_coins[-1]


class BottomUpMemoizationSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        few_coins = [-1] * (amount + 1)
        few_coins[0] = 0
        for cur_amount in range(1, len(few_coins)):
            for denomination in coins:
                last_amount = cur_amount - denomination
                if last_amount < 0:
                    continue
                if few_coins[last_amount] == -1:
                    continue
                if few_coins[cur_amount] > -1:
                    few_coins[cur_amount] = min(few_coins[last_amount] + 1,
                                                few_coins[cur_amount])
                else:
                    few_coins[cur_amount] = few_coins[last_amount] + 1
        return few_coins[-1]


class OptimizedBottomUpMemoizationSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        few_coins = [float('inf')] * (amount + 1)
        few_coins[0] = 0
        for denomination in coins:
            for cur_amount in range(denomination, len(few_coins)):
                few_coins[cur_amount] = min(
                    few_coins[cur_amount - denomination] + 1,
                    few_coins[cur_amount])
        return few_coins[-1] if few_coins[-1] != float('inf') else -1


Solution = OptimizedBottomUpMemoizationSolution
# @lc code=end
