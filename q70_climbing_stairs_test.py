from q70_climbing_stairs import Solution

solve = Solution().climbStairs


def test_default():
    assert solve(3) == 3


def test_corner_cases():
    assert solve(2) == 2
    assert solve(1) == 1
