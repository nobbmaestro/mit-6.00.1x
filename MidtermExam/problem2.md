# Problem 2
Multiple-choise Questions

## Problem 2-1
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
1. L is a list
2. L is immutable
3. L contains 6 elements
4. L has integer keys
5. L maps strings to integers

### Answer: 
> 5

## Problem 2-2
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?
1. The program might immediately terminate.
2. The function might immediately terminate.
3. The loop will always immediately terminate.
4. All of the above.
5. None of the above.

### Answer: 
> 3

## Problem 2-3
In Python, which of the following is a mutable object?
1. a string
2. a tuple
3. a list
4. all of the above
5. none of the above

### Answer: 
> 3

## Problem 2-4
Assume the statement s[1024] = 3 does not produce an error message. This implies:
1. type(s) can be str
2. type(s) can be tuple
3. type(s) can be list
4. All of the above

### Answer: 
> 4

## Problem 2-5
Consider the code:

>L = [1,2,3]<br>
d = {'a': 'b'}<br>
def f(x):<br>
    return 3<br>

Which of the following does NOT cause an exception to be thrown?
1. print(L[3])
2. print(d['b'])
3. for i in range(100001, -1, -2): print(f)
4. print(int('abc))
5. None of the above

### Answer: 
> 3

## Problem 2-6
Examine the following code snippet:

>stuff  = _____<br>
for thing in stuff:<br>
    if thing == 'iQ':<br>
       print("Found it")<br>

Select all the values of the variable "stuff" that will make the code print "Found it".
1. ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
2. ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
3. [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
4. ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
5. ["iQ"]
6. "iQ"

### Answer: 
> 1, 2 and 5

## Problem 2-7
The following Python code is supposed to compute the square of an integer by using successive additions.

>def Square(x):<br>
    return SquareHelper(abs(x), abs(x))<br><br>
def SquareHelper(n, x):<br>
    if n == 0:<br>
        return 0<br>
    return SquareHelper(n-1, x) + x<br>

Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.
1. It is going to return a wrong value.
2. The term Square is a reserved Python keyword.
3. Function names cannot start with a capital letter.
4. The function is never going to return anything.
5. Python has arbitrary precision arithmetic.
6. This function will not work for negative numbers.
7. The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
8. Nothing is wrong; the code is fine as-is.

### Answer: 
> 8