def repeat_char_jump(inputString, k):
    result = ''
    p = 0
    
    for _ in range(len(inputString)):
        result += inputString[p]
        p = (p + k) % len(inputString)
    
    return result