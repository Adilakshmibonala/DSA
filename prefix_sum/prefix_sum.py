import typing


def find_prefix_sum_approach1(input_array: typing.List[int], number_of_operations: int):
    """
    Time Complexity: O(n*number_of_operations)
    """
    prefixes = [[1, 2], [3, 5], [1, 6]]
    for each in range(number_of_operations):
        start, end = prefixes[each]
        prefix_sum = 0
        for i in range(start, end+1):
            prefix_sum += input_array[i]
        print(prefix_sum)


find_prefix_sum_approach1(input_array=[5, 2, -1, 6, -2, 7, 3], number_of_operations=3)
