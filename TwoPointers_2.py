from math import sqrt

def solution(numbers):
    # TODO: implement this function
    print("numbers: ", numbers)
    result = []
    n = len(numbers)
    for i in range(n):
        a = numbers[i]
        b = numbers[n - i - 1]
        result.append((a, round(sqrt(a * b), 2))) # Round to 2 decimal places
    print("result: ", result)
    return result

"""
Sample Output 1
numbers:  [1, 2, 3, 4, 5]  
result:  [(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)]  

Sample Output 2
numbers:  [3, 2, 1, 0, 1, 2, 3]  
result:  [(3, 3.0), (2, 2.0), (1, 1.0), (0, 0.0), (1, 1.0), (2, 2.0), (3, 3.0)]

Sample Output 3
numbers:  [100, 100]  
result:  [(100, 100.0), (100, 100.0)]
"""