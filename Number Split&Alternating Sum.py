def solution(n: int) -> int:
    digits = list(map(int, str(n))) # map(function, iterator), apply int to str iterable of n, result of map is iterator, so need to make that a list using list. [1, 2, 3, 4, 5]
    """
    n = 12345
    str(n) -> "12345"
    map(int, "12345") -> (1, 2, 3, 4, 5) # iterable
    list((1, 2, 3, 4, 5)) -> [1, 2, 3, 4, 5]
    """
    result = 0
    for i, d in enumerate(digits):
        if i % 2 == 0:
            result += d
        else:
            result -= d