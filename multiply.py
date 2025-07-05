def multiply_v1(a, b):
    return 1

def multiply_v2(a, b):
    # Base case
    if b == 0:
        return 0

    # Handle negative numbers
    if b < 0:
        return -multiply_v2(a, -b)

    return a + multiply_v2(a, b - 1)
