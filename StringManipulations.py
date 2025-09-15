def solution(inputString):
    result = ''
    l = 0
    r = len(inputString) - 1

    while l < r:
        result += inputString[l] + inputString[r]
        l += 1
        r -= 1

    if l == r:
        result += inputString[l]

    return result