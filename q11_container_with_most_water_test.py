from q11_container_with_most_water import Solution

solve = Solution().maxArea


def test_default():
    assert solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_corner_cases():
    assert solve([1, 2]) == 1
