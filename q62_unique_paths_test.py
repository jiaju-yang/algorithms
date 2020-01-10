from q62_unique_paths import Solution

solve = Solution().uniquePaths


def test_default():
    assert solve(3, 2) == 3
    assert solve(7, 3) == 28


def test_corner_cases():
    assert solve(2, 2) == 2
    assert solve(2, 1) == 1
    assert solve(1, 2) == 1
    assert solve(1, 1) == 1
