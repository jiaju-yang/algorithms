#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (37.53%)
# Likes:    3186
# Dislikes: 172
# Total Accepted:    439K
# Total Submissions: 1.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_len = max(map(len, wordDict + [""]))
        word_set = set(wordDict)
        dp = [True]

        for i in range(1, len(s) + 1):
            dp.append(
                any(s[j:i] in word_set and dp[j]
                    for j in range(max(i - max_word_len, 0), i)))
        return dp[-1]


class DPSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_be_segmented_before = [False] * len(s)

        for i in range(len(s)):
            char_i = i + 1
            for word in wordDict:
                word_len = len(word)
                if char_i - word_len < 0:
                    continue
                if s[char_i - word_len:char_i] == word and (
                        i - word_len == -1
                        or can_be_segmented_before[i - word_len]):
                    can_be_segmented_before[i] = True
                    break
        return can_be_segmented_before[-1]


# @lc code=end
