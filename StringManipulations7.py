# Capitalizing and Lowercasing String Words
def solution(input_str):
    chunks = input_str.split(" ") # ["some", "random", "_text"]
    output = []
    
    for chunk in chunks:
        word = list(chunk.lower()) # ['s', 'o', 'm', 'e']
        if word[0].isalnum():
            word[0] = word[0].upper()
        output.append(''.join(word))
    
    return " ".join(output)