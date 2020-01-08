from q322_coin_change import Solution

solve = Solution().coinChange


def test_default():
    assert solve([1, 2, 5], 11) == 3
    assert solve([186, 419, 83, 408], 6249) == 20


def test_not_found():
    assert solve([2], 3) == -1
    assert solve([3, 5], 7) == -1


def test_corner_cases():
    assert solve([1], 0) == 0
    assert solve([1], 1) == 1
