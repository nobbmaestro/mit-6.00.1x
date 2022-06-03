# Problem 3

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# output: Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# output: Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

def find_longest_substring_in_string(s):
    substring_count = 0
    list_of_strings = {0: s[0]}
    temp = ""
    for i in range(len(s)):
        temp = temp + s[i]
        try:
            if ord(s[i]) > ord(s[i+1]):
                list_of_strings[substring_count] = temp
                temp = ""
                substring_count += 1

        except IndexError:
            list_of_strings[substring_count] = temp

    list_of_lengths = []
    for i in list_of_strings:
        list_of_lengths.append(len(list_of_strings[i]))
    
    return list_of_strings[list_of_lengths.index(max(list_of_lengths))]

def main():
    list_of_strings = ['azcbobobegghakl', 'abcbcd']
    for s in list_of_strings:
        msg = "Longest substring in alphabetical order is: {substr}"
        print(msg.format(substr=find_longest_substring_in_string(s)))

if __name__ == '__main__':
    main()