"""Statues puzzle.
Given a list of statue sizes, determine how many additional statues are needed
to arrange them in consecutive order (each exactly 1 larger than the previous).
"""


def counter_of_extra_statues(statues):
    """Return how many statues are needed to make a consecutive sequence."""
    statues = sorted(statues)
    missing = 0

    for i in range(len(statues) - 1):
        difference = statues[i + 1] - statues[i]
        if difference > 1:
            missing += difference - 1

    return missing


user_statues = [6, 2, 3, 8]
print(counter_of_extra_statues(user_statues))
