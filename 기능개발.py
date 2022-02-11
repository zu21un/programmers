def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        if (progresses[i] / speeds[i]) > (progresses[i] // speeds[i]):
            progresses[i] = progresses[i] // speeds[i] + 1
        else:
            progresses[i] = progresses[i] // speeds[i]
    
    cnt = 1
    for i in range(1, len(progresses)):
        if progresses[i - cnt] < progresses[i]:
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
            
    answer.append(cnt)   
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))