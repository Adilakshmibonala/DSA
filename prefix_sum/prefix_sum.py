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


def find_prefix_sum(input_array: typing.List[int], number_of_operations: int):
    """
    Time Complexity: O(n+number_of_operations)
    """
    prefixes = [[1, 2], [3, 5], [1, 6]]
    prefix_sum_array = [input_array[0]]
    for index in range(1, len(input_array)):
        prefix_sum_array.append(input_array[index]+prefix_sum_array[index-1])

    for each in range(number_of_operations):
        start, end = prefixes[each]
        print(prefix_sum_array[end] - prefix_sum_array[start-1])


find_prefix_sum(input_array=[5, 2, -1, 6, -2, 7, 3], number_of_operations=3)
