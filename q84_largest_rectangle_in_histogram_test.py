from q84_largest_rectangle_in_histogram import Solution

solve = Solution().largestRectangleArea


def test_default():
    assert solve([2, 1, 5, 6, 2, 3]) == 10
    assert solve([2, 5, 4, 6, 4, 3]) == 16


def test_empty():
    assert solve([]) == 0


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([2]) == 2
    assert solve([3, 1]) == 3
    assert solve([1, 1]) == 2
    assert solve([2, 1, 2]) == 3
