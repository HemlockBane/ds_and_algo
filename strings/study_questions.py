# Input: s and t : strings
# Output: bool

# Input: s = "anagram", t = "nagaram"
# Output: true
# QED
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Input: s and t: str
# Output: true or false: bool

# We'll frequency count
# Loop through strings s and t, then store the chars
# and freqs for s in s_dict. do the same for t in the same loop
#  Loop through one of the maps and check if the value at that key
#  corresponds with the value at that key in the other map
# If there's a mismatch, return false early
# Once loop ends return true
def is_anagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for idx in range(len(s)):
        s_char = s[idx]
        t_char = t[idx]

        s_map[s_char] = s_map.get(s_char, 0) + 1
        t_map[t_char] = t_map.get(t_char, 0) + 1

    for k, v in s_map:
        if v != t_map.get(k):
            return False
    return True


# Longest substring without repeating characters
# Given a string s, find the length of the longest substring without repeating characters.

# Sample input: "abcabcbb"
# Expected output: 3

# We need a count and a map to store characters
# Double loop through the string
# if we have not seen a character in our current iteration (if map value is 0)
# - increase the freq of the char in the map
# - update max
# - update max_count if it is longer
# else
# - add item to map
# - break inner loop
def length_of_longest_substring_naive(s: str) -> int:
    max_count = 0
    for start_idx in range(len(s)):
        char_map = {}
        curr_count = 0
        for end_idx in range(start_idx, len(s)):
            curr_char = s[end_idx]
            curr_char_count = char_map.get(curr_char, 0)
            if curr_char_count != 0:
                break
            else:
                char_map[curr_char] = 1
                curr_count = curr_count + 1
                max_count = max(max_count, curr_count)

    return max_count


# Loop through string with a dynamic sliding window
# If char exists in map
# - Move window start forward until no duplicates exist in the window
# - reduce the curr window count
# Else
# - Add the char to map
# - update the window count
# - update the max count

# Sample input: "abcabcbb"
# Expected output:3
def length_of_longest_substring_optimised(s: str) -> int:
    window_start = 0
    curr_count = 0
    max_count = 0
    s_map = {}

    for window_end in range(len(s)):
        curr_count = curr_count + 1
        curr_char = s[window_end]
        char_frequency = s_map.get(curr_char, 0) + 1
        s_map[curr_char] = char_frequency

        while char_frequency > 1:
            char_frequency = char_frequency - 1
            s_map[curr_char] = char_frequency
            window_start = window_start + 1
            curr_count = curr_count - 1
        max_count = max(max_count, curr_count)

    return max_count
