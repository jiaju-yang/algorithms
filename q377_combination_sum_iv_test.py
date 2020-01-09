from q377_combination_sum_iv import Solution

solve = Solution().combinationSum4


def test_default():
    assert solve([1, 2, 3], 4) == 7
    assert solve([
        3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
        22, 23, 24, 25
    ], 10) == 9


def test_empty():
    assert solve([], 5) == 0
    assert solve([1], 0) == 0
