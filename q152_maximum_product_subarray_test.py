from q152_maximum_product_subarray import Solution

solve = Solution().maxProduct


def test_default():
    assert solve([2, 3, -2, 4]) == 6
    assert solve([-2, 0, -1]) == 0


def test_negative_integers():
    assert solve([-4, -3, -2]) == 12


def test_zero():
    assert solve([0, 0]) == 0


def test_corner_cases():
    assert solve([0]) == 0
    assert solve([1]) == 1
    assert solve([-1]) == -1