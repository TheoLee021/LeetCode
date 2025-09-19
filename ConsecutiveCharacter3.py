# using tuple

def solution(s):
    output = []
    current_char = None
    current_len = 0
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == current_char:
            current_len += 1
        else:
            if current_char != None:
                output.append((current_char, current_len))
            current_char = s[i]
            current_len = 1
            
    if current_char != None:
        output.append((current_char, current_len))
            
    return output