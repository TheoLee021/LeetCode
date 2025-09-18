def solution(numbers):
    mid = len(numbers) // 2

    if len(numbers) % 2 == 1:
        l = mid - 1
        r = mid + 1
        result = [numbers[mid]]
    else:
        l = mid - 1
        r = mid
        result = []
    
    while l >= 0 and r < len(numbers):
        result.append(numbers[l] * numbers[r])
        l -= 1
        r += 1

    return result

print(solution([1,2,3,4,5]))