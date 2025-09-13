def solution(n):
    duplicated_n = 0
    digits = 1
    while n > 0:
        digit = n % 10
        duplicated_n += (digit * digits) + (digit * digits * 10)
        digits *= 100
        n //= 10
    return duplicated_n