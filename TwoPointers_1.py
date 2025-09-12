def solution(numbers):
    print("numbers: ", numbers)
    n = len(numbers)
    result = []
    
    l = 0
    r = n - 1
    while l <= r:
        result.append(numbers[l] + numbers[r])
        l += 1
        r -= 1
    print("result: ", result)
    return result

"""
numbers:  [1, 2, 3, 4, 5]
result:  [6, 6, 6]

numbers:  [-5, -8, -10, -22, -12]
result:  [-17, -30, -20]

numbers:  [9, 98, -23, 4, -57]
result:  [-48, 102, -46]
"""