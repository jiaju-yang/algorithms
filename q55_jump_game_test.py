from q55_jump_game import Solution

solve = Solution().canJump


def test_default():
    assert solve([2, 3, 1, 1, 4]) is True
    assert solve([3, 2, 1, 0, 4]) is False


def test_corner_cases():
    assert solve([1]) is True
    assert solve([0]) is True
    assert solve([0, 1]) is False
    assert solve([1, 1]) is True


def test_empty():
    assert solve([]) is False
