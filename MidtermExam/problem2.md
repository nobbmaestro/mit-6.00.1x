# Problem 2
Multiple-choise Questions

## Problem 2-1
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
    a) L is a list
    b) L is immutable
    c) L contains 6 elements
    d) L has integer keys
    e) L maps strings to integers

### Answer: 
> e

## Problem 2-2
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?
    a) The program might immediately terminate.
    b) The function might immediately terminate.
    c) The loop will always immediately terminate.
    d) All of the above.
    e) None of the above.

### Answer: 
> c

## Problem 2-3
In Python, which of the following is a mutable object?
    a) a string
    b) a tuple
    c) a list
    d) all of the above
    e) none of the above

### Answer: 
> c

## Problem 2-4
Assume the statement s[1024] = 3 does not produce an error message. This implies:
    a) type(s) can be str
    b) type(s) can be tuple
    c) type(s) can be list
    d) All of the above

### Answer: 
> d

## Problem 2-5
Consider the code:

>L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

Which of the following does NOT cause an exception to be thrown?
    a) print(L[3])
    b) print(d['b'])
    c) for i in range(100001, -1, -2):
        print(f)
    d) print(int('abc))
    e) None of the above

### Answer: 
> c

## Problem 2-6
Examine the following code snippet:

>stuff  = _____
for thing in stuff:
    if thing == 'iQ':
       print("Found it")

Select all the values of the variable "stuff" that will make the code print "Found it".
    a) ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
    b) ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
    c) [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
    d) ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
    e) ["iQ"]
    f) "iQ"

### Answer: 
> a, b and e

## Problem 2-7
The following Python code is supposed to compute the square of an integer by using successive additions.

>def Square(x):
    return SquareHelper(abs(x), abs(x))

>def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.
    a) It is going to return a wrong value.
    b) The term Square is a reserved Python keyword.
    c) Function names cannot start with a capital letter.
    d) The function is never going to return anything.
    e) Python has arbitrary precision arithmetic.
    f) This function will not work for negative numbers.
    g) The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
    h) Nothing is wrong; the code is fine as-is.

### Answer: 
> h