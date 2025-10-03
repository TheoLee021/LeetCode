def replace_substring(text, old, new):
    if not old:
        return text
    
    output = []
    i = 0

    while True:
        start_point = text.find(old, i)
        if start_point == -1:
            output.append(text[i:]) # Adding remaing part
            break
        output.append(text[i:start_point]) # part before match
        output.append(new)
        i = start_point + len(old)
    
    return ''.join(output)