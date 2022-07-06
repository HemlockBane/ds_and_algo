from typing import List
#Given an array of integers and an integer target, find a subarray 
# that sums to target and return the start and end indices of the subarray.

# Input: Arr, target
# Output: start and end indices of matching range
# Sample data: [1 -20 -3 30 5 4] target: 7

# Assumptions: There's always one solution??

# Outer loop through the list to the second to the last element
# Inner loop from i + 1 to the last element
# For every subarray in range i to j, calculate the sum
# If sum is equal to target, return the start and end indices (right exclusive)

def subarray_sum_naive(arr: List[int], target: int) -> List[int]:
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            subarray_sum = sum(arr[i : j+1])
            if subarray_sum == target:
                return [i, j+1] # right exclusive


def subarray_sum_naive_2(arr: List[int], target: int) -> List[int]:
    for i in range(len(arr) - 1):
        subarray_sum = arr[i]
        for j in range(i+1, len(arr)):
            subarray_sum = subarray_sum + arr[j]
            if subarray_sum == target:
                return [i, j+1] # right exclusive


# This solution uses a map and the difference between cumulative sums to calculate 
# the sum of a subarray.
# The sum of a subarray is the difference between the cumulative sum at its start position
# and the cumulative sum at its end position
# Since we're looking for the subarray whose sum is equal to K,
# for each end position in our loop, we calculate the cumulative sum at that point,
# then we look for a suitable start position for our matching subarray 
# (i.e. what previous index has a cumulative sum such that the difference between
# that cumulative sum and the cumulative sum at our end position equals the target sum)

# Create a map to store the presums
# Loop through the list, for each end position
# - Find the cumulative sum that you need to subtract from your current
# - to give you the target value (i.e. cum_sum - target)
# - Check if that value exists in your map of cumulative sums
# - If it exists, get the index of that value, then return that index and the end index
def subarray_sum_optimised(arr: List[int], target: int) -> List[int]:
    pre_sums = {0:0}
    curr_sum = 0
    for end_idx in range(len(arr)):
        curr_sum = curr_sum + arr[end_idx]
        complement = curr_sum - target
        complement_idx = pre_sums.get(complement)
        if complement_idx is not None:
            return [complement_idx, end_idx + 1]

        pre_sums[curr_sum] = end_idx + 1




# Given an array of integers and an integer target, find the 
# number of subarrays which sums to target.

# Inputs: arr: List[int], target: int
# Outputs: count:int

# This is similar to subarray sum, but in this one we have complete the loop 
# (i.e. instead of breaking the loop when we find a match, we update our count instead.
# Once we're finished with the loop, we can the return the count)

# Loop through the list till the end
# For each end position
# - Update the cumulative sum
# - Check your presums for a cumulative sum such that the difference between your 
# - current cumulative sum and cumulative sum equals your target value
# - If it is not zero, update
def subarray_sum_count_optimised(arr: List[int], target: int) -> List[int]:
    pre_sums = {0:1}
    curr_sum = 0
    match_count = 0

    for end_idx in range(len(arr)):
        curr_sum = curr_sum + arr[end_idx]
        complement = curr_sum - target
        if complement in pre_sums:
            match_count = match_count + pre_sums[complement]
        curr_sum_freq = pre_sums[curr_sum] 
        pre_sums[curr_sum] =  curr_sum_freq + 1
    return match_count



# Input: nums = [1,2,3,4] - List[int]
# Output: [24,12,8,6] - List[int]

# Init our output list
# Loop through array
# At each index, we get the all the values before and after that index
# We find the product
# Then we add to output list
def product_except_self(nums: List[int]) -> List[int]:
    answer = []
    for i in range(len(nums)):
        before = nums[0:i]
        after = nums[i+1:]
        before.extend(after)

        product = 1
        for j in before:
            product = product * j
        answer.append(product)
    return answer
    
res = product_except_self([1,2,3,4])
print(res)
