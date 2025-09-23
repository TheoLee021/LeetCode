def parse_and_multiply_numbers(input_string): # "I have 2 apples and 5 oranges,"
    numbers = []
    for char in input_string:
        if char.isdigit():
            numbers.append(int(char))
    
    result = 1
    for num in numbers:
        result *= num

    return result

print(parse_and_multiply_numbers("I have 2 apples and 5 oranges,"))