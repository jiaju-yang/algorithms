from q300_longest_increasing_subsequence import Solution

solve = Solution().lengthOfLIS


def test_default():
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solve([10, 9, 2, 5, 3, 7, 101, 18, 20]) == 5
    assert solve([10, 9, 2, 5, 3, 4, 7, 101, 18]) == 5
    assert solve([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]) == 6


def test_empty():
    assert solve([]) == 0


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([1, 2]) == 2
    assert solve([3, 2]) == 1


def test_negative():
    assert solve([-2, -1]) == 2
