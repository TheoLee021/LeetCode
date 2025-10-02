def solution(strs, substrs):
    output = []
    for original, substring in zip(strs, substrs):
        start_pos = original.find(substring)
        match_indices = []
        while start_pos != -1:
            match_indices.append(str(start_pos))
            start_pos = original.find(substring, start_pos + 1)
        output.append(f"The substring '{substring}' was found in original string '{original}' at positions {', '.join(match_indices)}.")
    
    return output

print(solution(["HelloWorld", "LearningPython", "GoForBroke", "BackToBasics"], ["loW", "ear", "o", "Ba"]))