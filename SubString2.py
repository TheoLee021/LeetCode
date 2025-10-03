def replace_substring(text, old, new):
    start_pos = text.find(old)
    output = []
    
    if start_pos == -1:
        return text
    
    i = 0
    while i < start_pos:
        output.append(text[i])
        i += 1
        
    output.append(new)
    
    i = start_pos + len(old)
    start_pos = text.find(old, start_pos + len(old))
    if start_pos != -1:
        while i < start_pos:
            output.append(text[i])
            i += 1
        
        output.append(new)
    
        i = start_pos + len(old)
        
    while i < len(text):
        output.append(text[i])
        i += 1
    
    return ''.join(output)