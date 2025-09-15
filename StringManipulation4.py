def reversed_triple_chars(s: str) -> str:
    result = ''
    l = 0
    r = 2
    
    if len(s) < 3:
        return s
    
    while r < len(s):
        result += s[r] + s[l + 1] + s[l]
        l += 3
        r += 3
        
    if len(s) % 3 != 0:
        while l < len(s):
            result += s[l]
            l += 1
            
    return result

'''
List

def reversed_triple_chars(s: str) -> str:
    result = []
    l = 0
    r = 2
    
    if len(s) < 3:
        return s
    
    while r < len(s):
        result.append(s[r])
        result.append(s[l + 1])
        result.append(s[l])
        l += 3
        r += 3
        
    if l < len(s):
        result.append(s[l:])
            
    return ''.join(result)

Slicing

def reversed_triple_chars(s: str) -> str:
	result = []
	for i in range(0, len(s), 3):
		chunk = s[i:i+3]
		result.append(chunk[::-1] if len(chunk) == 3 else chunk)
	return ''.join(result)
'''