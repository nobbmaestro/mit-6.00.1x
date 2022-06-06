# Problem 1
#
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# >>> Number of vowels: 5

def count_vowels(s):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']

    num_vowels = 0
    for char in s:
        if char.lower() in list_of_vowels:
            num_vowels += 1

    return num_vowels

def main():
    s = 'azcbobobegghakl'
    msg = 'Number of vowels: {i}'
    print(msg.format(i=count_vowels(s)))

if __name__ == '__main__':
    main()