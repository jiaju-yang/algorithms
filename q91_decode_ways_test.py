from q91_decode_ways import Solution

solve = Solution().numDecodings


def test_default():
    assert solve('12') == 2
    assert solve('226') == 3


def test_empty():
    assert solve('') == 0


def test_corner_cases():
    assert solve('1') == 1
    assert solve('27') == 1


def test_zero():
    assert solve('0') == 0
    assert solve('01') == 0
    assert solve('306') == 0
    assert solve('106') == 1
