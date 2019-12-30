from q238_product_of_array_except_self import Solution

solve = Solution().productExceptSelf


def test_product():
    assert solve([4, 5, 1, 8, 2, 10,
                  6]) == [4800, 3840, 19200, 2400, 9600, 1920, 3200]
    assert solve([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_corner_cases():
    assert solve([1, 2]) == [2, 1]


def test_zero_numbers():
    assert solve([0, 1, 2]) == [2, 0, 0]
    assert solve([0, 0, 1, 2, 2]) == [0, 0, 0, 0, 0]
