from q198_house_robber import Solution

solve = Solution().rob


def test_default():
    assert solve([1, 2, 3, 1]) == 4
    assert solve([2, 7, 9, 3, 1]) == 12
    assert solve([2, 1, 1, 2]) == 4


def test_empty():
    assert solve([]) == 0


def test_corners():
    assert solve([1]) == 1
    assert solve([2, 1]) == 2
    assert solve([1, 3, 1]) == 3
    assert solve([1, 2, 3]) == 4
