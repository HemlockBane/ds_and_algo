from typing import List


# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
# Inputs: Arr, K
# Output: Arr of subarray averages
# Time complexity: O(n), space complexity: O(n)
# Example: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

# Outer loop from 0 to len - k + 1
# Inner loop from i to i + k
# For each element in the inner loop, find the sum of each element
# Once inner loop is done, find the average of sum save it in an array
# Once loop completes, return the array of averages

def k_avg_subarrays_naive(arr: List[int], size: int):
    averages = []
    for i in range(len(arr) - size + 1):
        curr_sum = 0
        for j in range(i, i + size):
            curr_sum = curr_sum + arr[j]
        avg = curr_sum / size
        averages.append(avg)
    return averages


# Time complexity: O(n), Space complexity: O(n)
# Loop through the list
# Calculate the sum
# If window end is greater than or equal to window size
# - Calculate the average and add it to the 
# - Update
def k_avg_subarrays_optimized(arr: List[int], size: int):
    window_sum = 0
    window_start = 0
    averages = []
    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]

        if window_end >= size - 1:
            avg = window_sum / size
            averages.append(avg)
            window_sum = window_sum - arr[window_start]
            window_start = window_start + 1
    return averages


# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k
# Inputs: array, size
# Output: max sum: int
# 
# Time complexity: O(n), Space complexity: O(1)

def k_max_sum_subarrays_naive(arr: List[int], size: int):
    max_sum = 0
    for i in range(len(arr) - size + 1):
        curr_sum = 0
        for j in range(i, i + size):
            curr_sum = curr_sum + arr[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


# Time complexity: O(n), Space complexity: O(1)
def k_max_sum_subarrays_optimised(arr: List[int], size: int) -> int:
    window_start = 0
    window_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]

        if window_end >= size - 1:
            max_sum = max(window_sum, max_sum)
            window_sum = window_sum - arr[window_end]
            window_start = window_start + 1
    return max_sum


# Given an array of positive integers and a number ‘S,’ find the 
# length of the smallest contiguous subarray whose sum is greater than 
# or equal to ‘S’. Return 0 if no such subarray exists.

# Inputs: Array, number S
# Outputs: length: int
# [2, 1, 5, 2, 3, 2], S=7

# Outer loop through the list from 0 to the end
# Inner loop through the list from i to the end
# If the current sum is greater than or equal to S
# - Find the length if the substring
# - If the length of the substring is smaller than smallest len but greater than 0, update smallest len

# Time complexity: O(n2), space complexity: O(1)
def smallest_subarray_sum_naive(arr: List[int], target: int):
    smallest_len = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum = curr_sum + arr[j]
            if curr_sum >= target:
                temp_len = len(arr[i:j + 1])
                if smallest_len != 0:
                    smallest_len = min(temp_len, smallest_len)
                else:
                    smallest_len = temp_len
    return smallest_len


# Outer loop through the list: each index is a window end
# Calculate the window sum
# If the window sum is greater than or equal to target
# - Update the smallest length
# - Keep moving the window start while window sum is greater than or equal to target
# -- Update the smallest length
# -- Update the window sum
# return the window sum

def smallest_subarray_sum_optimised(arr: List[int], target: int):
    window_sum = 0
    window_start = 0
    smallest_len = 0

    for window_end in range(len(arr)):
        window_sum = window_sum + arr[window_end]
        while window_sum >= target:
            temp_len = window_end - window_start + 1
            if smallest_len != 0:
                smallest_len = min(smallest_len, temp_len)
            else:
                smallest_len = temp_len
            window_sum = window_sum - arr[window_start]
            window_start = window_start + 1

    return smallest_len
