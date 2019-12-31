from q53_maximum_subarray import Solution

solve = Solution().maxSubArray


def test_default():
    assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_corner_cases():
    assert solve([2, 1]) == 3
    assert solve([2, -1]) == 2


def test_nagative_numbers():
    assert solve([-2, -1]) == -1
