from extra_0_1_knapsack import knap_sack


def test_default():
    assert knap_sack(50, [10, 20, 30], [60, 100, 120]) == 220
