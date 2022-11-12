import typing


def find_target_sum_subarray_approach1(input_array: typing.List[int], target_sum: int):
    """
    A basic approach
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





