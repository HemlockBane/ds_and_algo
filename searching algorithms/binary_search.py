from typing import List


# Binary search is an optimised way of search for a value in a sorted array
# It's a lot like using two pointers moving in opposite directions
# The idea is to continuously find the midpoint of the array, then compare our target value
# with the one at our midpoint.
# - If our target value is greater, we move the end pointer backwards
# - If our target value is lesser, we move the start pointer forwards
# - If our target value is equal, we have found our target
# We do this until the looping conditions are no longer met

# Input : List or String
# Output : Index of character (return - 1, if no matching character is found)
# Runtime: O(logn)
def binary_search(arr: List[str], target: str) -> int:
    start_ptr = 0
    end_ptr = len(arr) - 1

    while start_ptr <= end_ptr:
        mid_ptr = (start_ptr + end_ptr) // 2
        if arr[mid_ptr] == target:
            return mid_ptr
        elif arr[mid_ptr] < target:
            start_ptr = start_ptr + 1
        else:
            end_ptr = end_ptr + 1

    return -1
