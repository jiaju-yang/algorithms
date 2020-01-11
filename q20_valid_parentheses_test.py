from q20_valid_parentheses import Solution

solve = Solution().isValid


def test_default():
    assert solve('()') is True
    assert solve('()[]{}') is True
    assert solve('(]') is False
    assert solve('([)]') is False
    assert solve('{[]}') is True


def test_no_right_parenthesis():
    assert solve('{}(') is False
    assert solve('(') is False


def test_no_left_parenthesis():
    assert solve('){}') is False
    assert solve('{})') is False


def test_wrong_order():
    assert solve('{)(}') is False


def test_empty():
    assert solve('') is True
