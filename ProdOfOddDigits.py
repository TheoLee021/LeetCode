def solution(n):
    digit_prod = 1
    found = False # Boolean flag for a case no odd number
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            digit_prod *= digit
            found = True
        n = n // 10
    return digit_prod if found else 0 # Return 0 if there's no odd number