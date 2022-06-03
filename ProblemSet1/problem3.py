# Problem 3

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# output: Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# output: Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

import string

def find_longest_substring_in_string(s):
    temp = substring = s[0]
    list_of_substrings = []
    longest_substring = 0

    for char in s[1:]:
        if string.ascii_lowercase.index(temp) <= string.ascii_lowercase.index(char):
            substring += char
            temp = char
        else:
            list_of_substrings.append(substring)
            if len(substring) > len(list_of_substrings[longest_substring]):
                longest_substring = list_of_substrings.index(substring)
            substring = temp = char

    list_of_substrings.append(substring)
    return list_of_substrings[longest_substring]

def main():
    list_of_strings = ['azcbobobegghakl', 'abcbcd']
    for s in list_of_strings:
        msg = "Longest substring in alphabetical order is: {substr}"
        print(msg.format(substr=find_longest_substring_in_string(s)))

if __name__ == '__main__':
    main()