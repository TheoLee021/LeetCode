# Manipulating Strings: Reversing Words in a Sentence
def solution(s):
    chunk = []
    l = 0

    for i in range(len(s)):
        if s[i] == ' ':
            chunk.append(s[l:i][::-1])
            l = i + 1
    if s[-1] != ' ':
        chunk.append(s[l:][::-1])
    
    return ' '.join(chunk)

print(solution("Hello neat pythonistas_123"))