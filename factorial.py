def factorial(n):
    # since factorial doesnot work on negative numbers
    if n < 0:
        raise ValueError("Factorial does not suport negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)