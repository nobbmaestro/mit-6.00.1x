# Final Exam, Problem 2

## Problem 2-1

You have following class hierarchy:

```python
class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')
```

Which of the following is correct?

1. When *a = A()* we say that *a* is an instance of *A*
2. When *b = B()* we say that *b* is an instance of *A*
3. Both of the above
4. Neither of the above

### Answer

> A

## Problem 2-2

Consider the function f below. What is its Big O complexity?

```python
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)
```

### Answer

> O(n^2)

## Problem 2-3

A dictionary is an immutable object because its keys are immutable.

1. True
2. False because its keys can be mutable
3. False because a dictionary is mutable

### Answer

> 3

## Problem 2-4

Consider the following two functions and select the correct choice below:

```python
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1:
        return 1.0
    else:
        return n*foo_two(n-1)
```

1. The worst case Big Oh time complexity of *foo_one* is worse than the worst case Big Oh time complexity of *foo_two*.
2. The worst case Big Oh time complexity of *foo_two* is worse than the worst case Big Oh time complexity of *foo_one*.
3. The worst case Big Oh time complexity of *foo_one* and *foo_two* are the same.
4. Impossible to compare the worst case Big Oh time complexities of the two functions.

### Answer
>
> 3.

## Problem 2-5

The complexity of 1^n + n^4 + 4n + 4 is:

1. constant
2. logarithmic
3. linear
4. polynomial
5. exponential

### Answer

> 4
