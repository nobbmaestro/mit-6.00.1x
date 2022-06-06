# Problem 3

# Write a Python function, twoQuadratics, that takes in two sets of coefficients and x-values and prints the 
# sum of the results of evaluating two quadratic equations. It does not do anything else. That is, you should 
# evaluate and print the result of the following equation: 

# You are given the following function, evalQuadratic

# def evalQuadratic(a, b, c, x):
#    '''
#    a, b, c: numerical values for the coefficients of a quadratic equation
#    x: numerical value at which to evaluate the quadratic.
#    '''
#    return a*x*x + b*x + c
    
# Use the given function (you don't need to redefine evalQuadratic in this box; when you call evalQuadratic, our definition will be used).

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

def main():
    a1 = -5.36
    b1 = -3.18
    c1 = 0.38
    x1 = 2.34

    a2 = -4.39
    b2 = 6.79
    c2 = -8.75
    x2 = -5.3

    print(twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2))

if __name__ == '__main__':
    main()