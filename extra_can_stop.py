def can_stop(positions, speed):
    def can_stop_recursively(cur_p, cur_speed):
        if cur_p < 0 or cur_p >= len(positions):
            return False
        if cur_speed < 0:
            return False

        if positions[cur_p] is False:
            return False
        if cur_speed == 0:
            return True

        return can_stop_recursively(
            cur_p + cur_speed, cur_speed) or can_stop_recursively(
                cur_p + cur_speed - 1, cur_speed - 1) or can_stop_recursively(
                    cur_p + cur_speed + 1, cur_speed + 1)

    return can_stop_recursively(0, speed)
