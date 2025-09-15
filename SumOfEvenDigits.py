def solution(n):
    digit_sum = 0
    while n > 0:
        digit = n % 10 # extract the last digit
        if digit % 2 == 0:
            print(digit)
            digit_sum += digit
        n = n // 10 # remove the last digit
    return digit_sum

print(solution(4625))