def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))