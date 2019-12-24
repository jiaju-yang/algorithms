from q1_two_sum import Solution

solve = Solution().twoSum


def test_default():
    assert solve([2, 7, 11, 15], 9) == [0, 1]


def test_negative_input():
    assert solve([-3, 7, 11, 15, 1], -2) == [0, 4]


def test_empty_input():
    assert solve([2, 7, 11, 15], None) == []
    assert solve([], 5) == []
    assert solve([], None) == []


def test_invalid_input():
    assert solve([2], 5) == []


def test_not_found():
    assert solve([2, 7, 11, 16], 5) == []
