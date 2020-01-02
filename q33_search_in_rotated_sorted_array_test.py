from q33_search_in_rotated_sorted_array import Solution

solve = Solution().search


def test_default():
    assert solve([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solve([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_norotation():
    assert solve([2, 3, 4, 5], 3) == 1
    assert solve([2, 3, 4, 5], 6) == -1


def test_empty():
    assert solve([], 0) == -1
    assert solve(None, 3) == -1


def test_corner_cases():
    assert solve([2], 2) == 0
    assert solve([2], 1) == -1
