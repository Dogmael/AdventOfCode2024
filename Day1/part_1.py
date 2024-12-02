from helpers import get_lists


def compute_dist(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_dist = 0
    for left, right in zip(left_list, right_list):
        dist_diff = abs(right - left)  # Don't forget abs value !
        total_dist += dist_diff
    return total_dist


left_list, right_list = get_lists("input.txt")

total_dist = compute_dist(left_list, right_list)

print(total_dist)
