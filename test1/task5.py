def unique_chars_count(s):
    m=set(s)
    return len(m)
# create a set with the letters but without repetition
# then return the length

# Tests:

assert unique_chars_count("abcdef") == 6
assert unique_chars_count("aabbcc") == 3
assert unique_chars_count("abcabc") == 3
assert unique_chars_count("aaaaaa") == 1
assert unique_chars_count("") == 0