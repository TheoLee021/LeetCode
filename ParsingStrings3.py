# Parsing Sports Records: Calculating Sum of Scores
def solution(s):
    total = 0
    cur = []
    for c in s:
        if c.isdigit():
            cur.append(c)
        else:
            if cur:
                n = int(''.join(cur))
                if 1 <= n <= 100:
                    total += n
                cur = []
    if cur:
        n = int(''.join(cur))
        if 1 <= n <= 100:
            total += n
    
    return total

print(solution("jake scored1point, john scored2points"))