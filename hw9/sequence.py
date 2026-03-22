"""
Test the check_the_sequence function with several sample inputs
to verify it returns correct boolean results.
"""


def solution(users_arr: list) -> bool:
    """
    Check if the given list of integers can become strictly increasing
    by removing at most one element.
    """

    for i in range(1, len(users_arr)):
        if users_arr[i] <= users_arr[i - 1]:
            delete_current = users_arr[:i] + users_arr[i + 1:]
            delete_previous = users_arr[:i - 1] + users_arr[i:]
            is_current_ok = True
            for j in range(1, len(delete_current)):
                if delete_current[j] <= delete_current[j - 1]:
                    is_current_ok = False
                    break
            is_previous_ok = True
            for k in range(1, len(delete_previous)):
                if delete_previous[k] <= delete_previous[k - 1]:
                    is_previous_ok = False
                    break
            if is_current_ok or is_previous_ok:
                return True
            return False
    return True


assert solution([1, 2, 3])
assert not solution([1, 2, 1, 2])
assert not solution([1, 3, 2, 1])
assert not solution([1, 2, 3, 4, 5, 3, 5, 6])
assert not solution([40, 50, 60, 10, 20, 30])

print('ok')
