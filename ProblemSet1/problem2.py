# Problem 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print following
# > Number of times bob occurs is: 2

def bob_in_string_count(s):
    numBob = 0
    for i in range(len(s)-2):
        temp = s[i] + s[i+1] + s[i+2]
        if temp == 'bob':
            numBob += 1

    return numBob
    

def main():
    s = 'azcbobobegghakl'
    msg = 'Number of times bob accurs is: {i}'
    print(msg.format(i=bob_in_string_count(s)))

if __name__ == '__main__':
    main()