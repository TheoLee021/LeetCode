def special_order(inputString):
    result = ''
    l = 0
    r = len(inputString) - 1
    
    while r >= len(inputString) // 2:
        result += inputString[r]
        r -= 1
    
    while l <= r:
        result += inputString[l]
        l += 1
        
    return result