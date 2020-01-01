from q153_find_minimum_in_rotated_sorted_array import Solution

solve = Solution().findMin


def test_default():
    assert solve([3, 4, 5, 1, 2]) == 1
    assert solve([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solve([7, 1, 2, 3, 4, 5]) == 1


def test_corner_cases():
    assert solve([2, 1]) == 1
    assert solve([1, 2]) == 1


def test_empty():
    assert solve([]) is None
    assert solve(None) is None


def test_only_one_element():
    assert solve([1]) == 1


def test_no_rotation():
    assert solve([1, 2, 3, 4, 5]) == 1


def test_negative():
    assert solve([0, 1, 2, -3, -2]) == -3
    assert solve([-4, -3, -2, -1, -6, -5]) == -6