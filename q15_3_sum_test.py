from q15_3_sum import Solution

solve = Solution().threeSum


def test_default():
    # assert solve([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solve([-1, 0, 1, 2, -1, -3, -4]) == [[-3, 1, 2], [-1, -1, 2],
                                                [-1, 0, 1]]


def test_invalid():
    assert solve([]) == []
    assert solve([1]) == []
    assert solve([1, 2]) == []


def test_corner_cases():
    assert solve([1, 2, 3]) == []
    assert solve([1, 2, -3]) == [[-3, 1, 2]]


def test_duplicated():
    assert solve([1, 1, 2, -3]) == [[-3, 1, 2]]
    assert solve([1, 1, -2, -3]) == [[-2, 1, 1]]
