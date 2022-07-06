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


# You are given an array prices where prices[i] is the 
# price of a given stock on the ith day.

# Inputs - prices: List[int]
# Output - max profit: int

# Sample: [7,1,5,3,6,4] => 5
# [7,6,4,3,1] => 0

# Init max_profit
# Outer loop through the array till the second to the last
# Inner loop through the array from i + 1 to end
# - If j - 1 > max_profit, update max_profit
# Return max_profit

# Time complexity: O(n2); Space complexity: O(1)
def get_max_profit_naive(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def get_max_profit_optimised(prices: List[int]) -> int:
    max_profit = 0
    pass

res = get_max_profit_naive([7,6,4,3,1])
print(res)

#Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: arr: List[int], target: int
# Output: min len of contig subarrays with sum >= target

