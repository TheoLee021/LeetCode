def unusual_traversal(array):
    mid = len(array) // 2
    if len(array) % 2 == 1:
        l = mid - 1
        r = mid + 1
        result = [array[mid]]
    else:
        l = mid - 1
        r = mid
        result = []
        
    while l >= 0 and r < len(array):
        if l == 0:
            result.append(array[l])
        else:
            result.append(array[l - 1])
            result.append(array[l])
        if r == len(array) - 1:
            result.append(array[r])
        else:
            result.append(array[r])
            result.append(array[r + 1])
        l -= 2
        r += 2

    return result