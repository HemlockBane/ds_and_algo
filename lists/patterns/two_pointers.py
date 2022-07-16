from typing import List


# Items are sorted, use in place sorting_algorithms, no aux data structure allowed
# Input: a list of integers
# Output: the new length of the list without duplicates
# O(n)
def remove_duplicates(nums: List[int]) -> int:
    # Generally, we use 2 pointers moving in the same direction: one fast, one slow
    # We loop through the nums,
    # slow_ptr starts at 0
    # If the item at slow_ptr == item at fast_ptr,
    # - increase the slow_ptr by 1
    # - set the item at the slow_ptr index to the item at the fast_ptr index
    # Once the loop completes, return length of filtered subarray (slow_ptr index + 1)

    slow_ptr = 0
    for fast_ptr in range(len(nums)):
        if nums[slow_ptr] == nums[fast_ptr]:
            slow_ptr = slow_ptr + 1
            nums[slow_ptr] = nums[fast_ptr]
    return slow_ptr + 1
