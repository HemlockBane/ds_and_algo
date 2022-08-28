from typing import List


# Check if a given parentheses string is valid
#
# Input: par: string
# Output: true or false: bool
#
# We need a stack to store opening braces
# We need a map to store types of braces
#
# Check the length of the string, if the length is odd, return False
# Loop through the list, for each char,
# - If it is an opening brace, add it to the stack
# - If it is not an opening brace,
# -- If the stack is empty, return False
# -- Pop the stack and get the next opening brace
# --- If char is not equal to value at map with key opening brace , return False
# Return whether the stack is empty:
# - if there's an item left when the loop is done, the string is clearly unbalanced
def is_valid(par_str: str) -> bool:
    stack = []
    par_map = {"{": "}", "[": "]", "(": ")"}

    if len(par_str) % 2 != 0:
        return False

    for char in par_str:
        if char in par_map.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            open_brac = stack.pop()
            if char != par_map[open_brac]:
                return False
    return stack == []


# Find the number of indices till you find a warmer temperature

# We use a stack to store the future items
# We use a list to store our answers
#
# We traverse the temperature list in reverse:
# - We keep checking if our stack has values and if our current temperature
# is greater than or equal to our next value in the stack. If true, pop the stack
# - We check if the stack is not empty and if our current temperature is less than
# the next value in the stack. If true, find the difference between
# the stack index and the index of the current temperature
# - Add the current index to the stack
#
# Return results

def get_daily_temperatures(temps: List[int]) -> List[int]:
    arr_len = len(temps)

    stack = []
    results = [0] * arr_len

    for curr_idx in range(arr_len - 1, -1, -1):
        while len(stack) != 0 and temps[curr_idx] >= temps[stack[-1]]:
            stack.pop()

        if len(stack) != 0 and temps[curr_idx] < temps[stack[-1]]:
            diff = stack[-1] - curr_idx
            results[curr_idx] = diff

        stack.append(curr_idx)

    return results
