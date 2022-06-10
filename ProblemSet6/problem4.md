# Problem 4
Select the correct option from list:
- O(1)
- O(log(n))
- O(n)
- O(n log(n))
- O(n^2)
- O(n^3)
- O(2^n)

## Problem 1-1
Consider the following Python procedure. Specify its order of growth.
```python
def modten(n):
    return n%10
```

### Answer: 
> O(1)

## Problem 1-2
Consider the following Python procedure. Specify its order of growth.
```python
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result 
```
### Answer: 
> O(len(n))

## Problem 1-3
Consider the following Python procedure. Specify its order of growth.
```python
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
```

### Answer: 
> O(log(n))

## Problem 1-4
Consider the following Python procedure. Specify its order of growth.
```python
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
```

### Answer: 
> O(n log(n))

## Problem 1-5
Consider the following Python procedure. Specify its order of growth.
```python
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
```

### Answer: 
> O(n^2)