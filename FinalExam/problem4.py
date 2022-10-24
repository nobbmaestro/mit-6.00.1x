"""Final Exam, Problem 4.

Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in
increasing order. A prime number is a number that is divisible only by 1 and itself. This function takes in an
integer and returns a list of integers.
"""


# pylint: disable=C0103
def primes_list(N):
    """Return a list of prime numbers between 2 and N.

    Args:
        N (int): highiest prime

    Returns:
        list: list of primes
    """
    lift_of_primes = list(range(2, N + 1, 1))
    for prime in lift_of_primes:
        for number in lift_of_primes:
            if number > prime and number % prime == 0:
                lift_of_primes.remove(number)

    return lift_of_primes
