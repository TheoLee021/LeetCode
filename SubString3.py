# Spotting Swapped Characters in Strings
def spot_swaps(source: str, target: str) -> list:
    l = 0
    r = 1
    size = len(source)
    output = []
    
    while r < size:
        if source[l] != target[l]:
            if source[l] == target[r]:
                if source[r] == target[l]:
                    output.append((l, source[l], target[l]))
        l += 1
        r += 1
        
    return output