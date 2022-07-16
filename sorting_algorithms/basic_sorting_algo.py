from typing import List


# Bubble Sort:
# TL;DR - stable & in-place sort: Gradually bubble up the highest value
# Bubble sort works by gradually moving the highest value to the end
# You have to compare each adjacent value in the swapping range
# to find the highest value,then swap when the next item is higher.
# NB: Your swapping range reduces gradually for each iteration. The idea is that
#

# Runtime: log(n ^ 2) - Very bad

# Let's use a double loop
# In the outer loop, let's loop to the second to last element:
# - This represents our total number of iterations
# In the inner loop, let's compare all the values in our swapping range
# - Swapping range increases for each outer loop iteration
# - If we, see a higher value, swap
# [-2, 45, 0, 11, -9]

def bubble_sort_naive(arr: List):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


# We just make an optimisation for sorted lists:
# When the list is already sorted (i.e. no swap), we stop checking
# The naive version still checks even when list is sorted
def bubble_sort_optimised(arr: List):
    for i in range(len(arr) - 1):
        is_swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                is_swapped = True

        if not is_swapped:
            return arr
    return arr


# Selection Sort;
# TL:DR -  unstable & in-place sort: Gradually sort by finding min
# Outer loop to the second to the last item
# - Set min idx to current iteration
# - Inner loop (from current iteration + 1) to the last element
# -- If element at current inner loop iteration < element at min idx, update min idx
# - swap element at current outer loop iteration with element at min idx

# Runtime: O(n)

def selection_sort(arr: List):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr
