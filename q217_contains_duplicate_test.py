from q217_contains_duplicate import Solution

solve = Solution().containsDuplicate


def test_duplicated():
    assert solve([1, 2, 3, 1]) is True
    assert solve([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_no_duplicated():
    assert solve([1, 2, 3, 4]) is False


def test_empty_input():
    assert solve([]) is False


def test_only_one_value_input():
    assert solve([1]) is False


def test_corner_cases():
    assert solve([1, 1]) is True
    assert solve([1, 2]) is False
