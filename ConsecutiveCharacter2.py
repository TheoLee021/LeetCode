# Run-Length Encoding(RLE)

def encode_rle(s):
    result = ''
    current_char = None
    current_len = 0
    
    for c in s:
        if not c.isalnum():
            continue
        
        if c == current_char:
            current_len += 1
        else:
            if current_char != None:
                result += current_char + str(current_len)
            current_char = c
            current_len = 1
        
    if current_char != None:
        result += current_char + str(current_len)
        
    return result