from q213_house_robber_ii import Solution

solve = Solution().rob


def test_default():
    assert solve([2, 3, 2]) == 3
    assert solve([1, 2, 3, 1]) == 4


def test_empty():
    assert solve([]) == 0


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([1, 2]) == 2
    assert solve([1, 2, 3]) == 3
