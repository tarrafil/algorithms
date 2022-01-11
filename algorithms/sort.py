""" sort module """

import utils


def bubble_sort(sequence: list) -> list:
    """Simple implementation of the bubble sort algorithm in Python
    :param sequence: some mutable ordered collection with heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    """

    if len(sequence) < 2:
        return sequence
    _sequence = sequence[:]

    length = len(_sequence)
    swapped = False
    for i in range(length - 1):
        if _sequence[i] > _sequence[i+1]:
            _sequence[i], _sequence[i+1] = _sequence[i+1], _sequence[i]
            swapped = True
    return _sequence if not swapped else bubble_sort(_sequence)


def heap_sort(sequence: list) -> list:
    """Simple implementation of the heap sort algorithm in Python
    :param sequence: some mutable ordered collection with heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    """

    if len(sequence) < 2:
        return sequence
    _sequence = sequence[:]

    def heapify(seq, index, heap_size):
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < heap_size and seq[left_index] > seq[largest]:
            largest = left_index
        if right_index < heap_size and seq[right_index] > seq[largest]:
            largest = right_index
        if largest != index:
            seq[largest], seq[index] = seq[index], seq[largest]
            heapify(seq, largest, heap_size)

    length = len(_sequence)
    for i in range(length // 2 - 1, -1, -1):
        heapify(_sequence, i, length)
    for i in range(length - 1, 0, -1):
        _sequence[0], _sequence[i] = _sequence[i], _sequence[0]
        heapify(_sequence, 0, i)
    return _sequence


def merge_sort(sequence: list) -> list:
    """Simple implementation of the merge sort algorithm in Python
    :param sequence: some mutable ordered collection with heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    """

    if len(sequence) < 2:
        return sequence
    _sequence = sequence[:]

    def merge(left: list, right: list) -> list:
        seq = []
        while left and right:
            seq.append((left if right[0] > left[0] else right).pop(0))
        return seq + left + right

    mid = len(_sequence) // 2
    return merge(merge_sort(_sequence[:mid]), merge_sort(_sequence[mid:]))


def quick_sort(sequence: list) -> list:
    """Simple implementation of the quick sort algorithm in Python
    :param sequence: some mutable ordered collection with heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    """

    if len(sequence) < 2:
        return sequence
    _sequence = sequence[:]

    pivot = _sequence.pop()
    lesser = []
    greater = []
    for element in _sequence:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    _list = utils.random_list_int()
    assert bubble_sort(_list) == sorted(_list)
    _list = utils.random_list_int()
    assert heap_sort(_list) == sorted(_list)
    _list = utils.random_list_int()
    assert merge_sort(_list) == sorted(_list)
    _list = utils.random_list_int()
    assert quick_sort(_list) == sorted(_list)
