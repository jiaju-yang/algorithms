#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.31%)
# Likes:    1963
# Dislikes: 2216
# Total Accepted:    328.2K
# Total Submissions: 1.4M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        previous_count, previous_two_chars_count = 0 if s[0] == '0' else 1, 1
        for i in range(1, len(s)):
            one_digit = int(s[i])
            two_digits = int(s[i - 1:i + 1])
            current_count = 0
            if 1 <= one_digit <= 9:
                current_count += previous_count
            if 10 <= two_digits <= 26:
                current_count += previous_two_chars_count
            previous_count, previous_two_chars_count = current_count, previous_count
        return previous_count


# @lc code=end
