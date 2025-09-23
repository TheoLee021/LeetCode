def solution(input_str):
    chunks = input_str.split(" ") # ["CapitaL", "letters"]
    output = []
    for chunk in chunks: # ["CapitaL"]
        words = []
        for char in chunk:
            if char.isupper():
                words.append(chr(26 - (ord(char) - ord('A') + 1) + ord('A')))
            else:
                words.append(chr(26 - (ord(char) - ord('a') + 1) + ord('a')))
        # ['X', 'z', 'k', 'r', 'g', 'z', 'O']
        output.append(''.join(words)) # ['XzkrgzO']
    
    if len(output) > 1:
        output = [output[-1]] + output[:-1]
    
    return ' '.join(output)