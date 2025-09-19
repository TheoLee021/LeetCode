def solution(string):
    result = []
    current_char = None
    current_len = 0

    for char in string:
        if char.isalnum():
            if char == current_char:
                current_len += 1
            else:
                if current_char != None:
                    result.append((current_char, current_len))
                current_char = char
                current_len = 1

    if current_char != None:
        result.append((current_char, current_len))

    return result