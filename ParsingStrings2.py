# Parsing and Converting Words in a String
def solution(s):
    chars = s.split('-') # ['1','a','3']
    output = []
    for char in chars:
        if char.isdigit():
            output.append(chr(ord('a') + int(char) - 1))
        elif char.isalpha():
            output.append(str(ord(char) - ord('a') + 1))
    
    return '-'.join(output)