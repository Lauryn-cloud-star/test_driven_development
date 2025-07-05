def multiply_1 (a, b):
    return 1

# carringout the multiplication using repeated addition
def multiply(a, b):
    
    result = 0
    
    # abs function is used to handle negative numbers hence they are handled in that case as positive
    # the loop runs for the absolute value of b, adding a to result each time
    # if b is negative, the result is negated at the end
    for i in range(abs(b)):
    # adding a to result for each iteration
        result += a
    return result if b > 0 else -result

