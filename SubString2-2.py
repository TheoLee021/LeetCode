def replace_substring(text, old, new):
    if not old:
        return text
    
    output = []
    i = 0

    while True:
        start_point = text.find(old, i)
        if start_point == -1:
            output.append(text[i:]) # 남은 꼬리 붙이기
            break
        output.append(text[i:start_point]) # 매치 전 구간
        output.append(new)
        i = start_point + len(old)
    
    return ''.join(output)