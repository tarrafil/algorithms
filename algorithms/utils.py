""" utils module"""

import random


def random_list_int(length: int = 10, lower_bound: int = -100, upper_bound: int = 100) -> list:
    random_list = []
    while len(random_list) < length:
        n = random.randint(lower_bound, upper_bound)
        random_list.append(n)
    return random_list


def reverse(sequence: list) -> list:
    _sequence = []
    while sequence:
        _sequence.append(sequence.pop())
    return _sequence
