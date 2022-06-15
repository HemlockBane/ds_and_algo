from typing import List


# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

def get_k_average_subarrays_naive(arr: List[int], size: int):
    results = []
    for i in range(len(arr) - size + 1):
        _sum = 0
        for j in range(i, i + size):
            _sum = _sum + arr[j]
        results.append(_sum / size)
    print(results)


def get_k_average_subarrays_optimised(arr: List[int], size: int):
    # loop through the list: each index is a potential window end
    # We'll need a window start, and  sum
    # We'll need to store all the averages too
    # Keep calculating the window sum
    # if the window end has reached the max window size,
    # - Calculate and store the average
    # - update the window sum
    # - move the window start
    results = []
    w_start = 0
    w_sum = 0
    for w_end in range(len(arr)):
        w_sum = arr[w_end] + w_sum

        # Window has reached window size
        if w_end >= size - 1:
            avg = w_sum / size
            results.append(avg)
            w_sum = w_sum - arr[w_start]
            w_start = w_start + 1
    print(results)

    # Given an array of positive numbers and a positive number ‘k,’ find the maximum sum
    # of any contiguous subarray of size ‘k’.

    # positive
    # input: an array, window size
    # output: max sum: int


def get_k_max_sum_from_subarrays_naive(arr: List[int], size: int):
    # Outer Loop through the list from 0 to max possible window_start
    # Inner loop through the list from i to window end
    # - Calculate the running sum
    # - Once the inner loop ends, if, the current running sum is greater than max sum, update the max sum

    max_sum = 0
    for i in range(len(arr) - size + 1):
        curr_sum = 0
        for j in range(i, i + size):
            curr_sum = curr_sum + arr[j]
        max_sum = max(curr_sum, max_sum)
    print(max_sum)


def get_k_max_sum_from_subarrays_optmised(arr: List[int], size: int):
    # We need something to track max sum
    # We need to track window start and window sum
    # We loop to the end of the list
    # We calculate the window sum
    # If the window end is greater than or equal to size - 1,
    # - update the max sum
    # - update the window sum
    # - update the window start

    w_start = 0
    w_sum = 0
    max_sum = 0

    for w_end in range(len(arr)):
        w_sum = w_sum + arr[w_end]

        if w_end >= size - 1:
            max_sum = max(max_sum, w_sum)
            w_sum = w_sum - arr[w_start]
            w_start = w_start + 1

    print(max_sum)

