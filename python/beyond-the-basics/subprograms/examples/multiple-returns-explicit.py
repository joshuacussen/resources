def division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return (quotient, remainder)


results = division(23, 5)  # results = (4, 3)
q, r = division(19, 2)  # q = 9, r = 1
