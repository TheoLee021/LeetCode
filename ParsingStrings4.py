# Shifting Characters within a String Following Numerical Values
def solution(input_string):
    n = len(input_string)
    output = []
    i = 0

    while i < len(input_string):
        c = input_string[i]
        if c.isdigit():
            j = i
            while j < n and input_string[j].isdigit():
                j += 1
            num = input_string[i:j]

            k = j
            while k < n and not input_string[k].isalpha():
                k += 1
            output.append(input_string[k])
            output.append(num)
            i = k + 1

        else:
            output.append(input_string[i])
            i += 1
    
    return ''.join(output)

print(solution("I have 2 apples and 5! oranges and 3 grapefruits."))