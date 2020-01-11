from q42_trapping_rain_water import Solution

solve = Solution().trap


def test_default():
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_empty():
    assert solve([]) == 0


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([1, 2]) == 0
    assert solve([1, 2, 1]) == 0
    assert solve([2, 1, 2]) == 1
