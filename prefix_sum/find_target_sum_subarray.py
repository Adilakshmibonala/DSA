import typing


def find_target_sum_subarray_approach1(input_array: typing.List[int], target_sum: int):
    """
    A basic approach

    Outer loop iterates n times in worst case.
    Inner loop iterates n times in worst case.
    Time Complexity: O(n^2)
    """
    array_len = len(input_array)
    for index, element in enumerate(input_array):
        current_sum = element
        for each in range(index+1, array_len):
            if current_sum == target_sum:
                for i in range(index, each):
                    print(input_array[i], end=" ")
                break
            elif current_sum > target_sum:
                break
            else:
                current_sum += input_array[each]


find_target_sum_subarray_approach1(input_array=[10, 44, 20, 2, 10, 5], target_sum=32)


def find_target_sum_subarray_using_sliding_window_approach(
        input_array: typing.List[int], target_sum: int):
    """
    Time complexity: O(n)
    """
    array_len = len(input_array)
    current_sum, start_index = 0, 0
    for index, element in enumerate(input_array):
        while current_sum > target_sum and start_index < array_len:
            current_sum -= input_array[start_index]
            start_index += 1
        if current_sum == target_sum:
            for i in range(start_index, index):
                print(input_array[i], end=" ")
            break
        else:
            current_sum += input_array[index]


find_target_sum_subarray_using_sliding_window_approach(input_array=[10, 44, 20, 2, 10, 5], target_sum=32)

