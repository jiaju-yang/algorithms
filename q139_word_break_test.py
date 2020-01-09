from q139_word_break import Solution

solve = Solution().wordBreak


def test_default():
    assert solve("leetcode", ["leet", "code"]) is True
    assert solve("applepenapple", ["apple", "pen"]) is True
    assert solve("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_empty():
    assert solve("a", []) is False
    assert solve("", []) is True
