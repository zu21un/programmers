def solution(brown, yellow):
    length = (brown // 2) + 2
    for i in range(1, length):
        if i * (length - i) == brown + yellow:
            return [length - i, i]
        
print(solution(10,2))