a = [0, 1, 2, 3, 4]

def solution(a):
    b = [0 for _ in range(len(a))]
    for i in range(len(a) - 1):
        if i == 0:
            b[i] = a[i] + a[i + 1]
        elif i == len(a) - 1:
            b[i] = a[i - 1] + a[i]
        else:
            b[i] = a[i - 1] + a[i] + a[i + 1]
    return b

print(solution(a))