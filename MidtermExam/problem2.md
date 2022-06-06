# Problem 2
Multiple-choise Questions

## Problem 2-1
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?

### Answer: 
>- [] L is a list
- [] L is immutable
- [] L contains 6 elements
- [] L has integer keys
- [x] L maps strings to integers

### Answer: 


## Problem 2-2
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?

### Answer: 
>- [] The program might immediately terminate.
- [] The function might immediately terminate.
- [x] The loop will always immediately terminate.
- [] All of the above.
- [] None of the above.

## Problem 2-3
In Python, which of the following is a mutable object?

### Answer: 
>- [] a string
- [] a tuple
- [x] a list
- [] All of the above
- [] None of the above

## Problem 2-4
Assume the statement s[1024] = 3 does not produce an error message. This implies:

### Answer: 
>- [] type(s) can be str
- [] type(s) can be tuple
- [] type(s) can be list
- [x] All of the above


## Problem 2-5
Consider the code:

>L = [1,2,3]<br>
d = {'a': 'b'}<br>
def f(x):<br>
    return 3<br>

Which of the following does NOT cause an exception to be thrown?

### Answer: 
>- [] print(L[3])
- [] print(d['b'])
- [x] for i in range(100001, -1, -2):
print(f)
- [] print(int('abc))
- [] None of the above

## Problem 2-6
Examine the following code snippet:

>stuff  = _____<br>
for thing in stuff:<br>
    if thing == 'iQ':<br>
       print("Found it")<br>

Select all the values of the variable "stuff" that will make the code print "Found it".

### Answer: 
>- [x] ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
- [x] ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
- [] [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
- [] ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
- [x] ["iQ"]
- [] "iQ"

## Problem 2-7
The following Python code is supposed to compute the square of an integer by using successive additions.

>def Square(x):<br>
    return SquareHelper(abs(x), abs(x))<br><br>
def SquareHelper(n, x):<br>
    if n == 0:<br>
        return 0<br>
    return SquareHelper(n-1, x) + x<br>

Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.

### Answer: 
>- [] It is going to return a wrong value.
- [] The term Square is a reserved Python keyword.
- [] Function names cannot start with a capital letter.
- [] The function is never going to return anything.
- [] Python has arbitrary precision arithmetic.
- [] This function will not work for negative numbers.
- [] The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
- [x] Nothing is wrong; the code is fine as-is.