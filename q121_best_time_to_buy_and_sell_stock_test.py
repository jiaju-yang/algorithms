from q121_best_time_to_buy_and_sell_stock import Solution

solve = Solution().maxProfit


def test_default():
    assert solve([7, 1, 5, 3, 6, 4]) == 5


def test_corner_cases():
    assert solve([1, 2]) == 1
    assert solve([2, 1]) == 0


def test_no_transaction():
    assert solve([7, 6, 4, 3, 1]) == 0


def test_empty_input():
    assert solve(None) == 0
    assert solve([]) == 0


def test_invalid_input():
    assert solve([1]) == 0
