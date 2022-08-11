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



