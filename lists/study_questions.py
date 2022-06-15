from typing import List


# O(n2)
# inputs: array of integers & a number (int, int)
# output:return a list of the matching values
def two_sum_naive(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# O(n)
# inputs: array of integers & a number (int, int)
# output:return a list of the matching values
def two_sum_optimised(nums: List[int], target: int) -> List[int]:
    _map = {}
    for num_idx in range(len(nums)):
        num = nums[num_idx]
        pair = target - num
        pair_idx = _map.get(pair)
        if pair_idx is not None:
            return [num_idx, pair_idx]
        _map[num] = num_idx

    return []


# In place, constant auxiliary space
# Input: An array of integers
# Output: The array of integers but with thw zeros to the back

def move_zeros(nums: List[int]) -> None:
    pass
