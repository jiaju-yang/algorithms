def knap_sack(capacity, weights, values):
    stored_knap_sack = [[c for c in range(capacity + 1)]
                        for _ in range(len(weights))]
    for i in range(len(weights)):
        for c in range(capacity + 1):
            if c < weights[0]:
                stored_knap_sack[i][c] = 0
            elif i == 0:
                stored_knap_sack[i][c] = values[i]
            else:
                stored_knap_sack[i][c] = max(
                    stored_knap_sack[i - 1][c],
                    stored_knap_sack[i - 1][c - weights[i]] + values[i])
    return stored_knap_sack[len(weights) - 1][capacity]


def knap_sack_recursively(capacity, weights, values):
    if not weights:
        return 0
    if capacity < weights[0]:
        return 0

    return max(
        knap_sack_recursively(capacity, weights[:-1], values[:-1]),
        knap_sack_recursively(capacity - weights[-1], weights[:-1],
                              values[:-1]) + values[-1])
