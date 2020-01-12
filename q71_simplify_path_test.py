from q71_simplify_path import Solution

solve = Solution().simplifyPath


def test_end_with_slash():
    assert solve('/home/') == '/home'
    assert solve('/a/./b/../../c/') == '/c'
    assert solve('/a/../../b/../c//.//') == '/c'


def test_empty():
    assert solve('') == '/'
    assert solve('/') == '/'
    assert solve('//') == '/'


def test_several_slashs():
    assert solve('/home//foo/') == '/home/foo'
    assert solve('/a//b////c/d//././/..') == '/a/b/c'


def test_double_period():
    assert solve('/../') == '/'
    assert solve('/a/..') == '/'


def test_single_period():
    assert solve('/./') == '/'
    assert solve('/a/.') == '/a'
