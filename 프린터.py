def solution(priorities, location):
    sorted_priorities = sorted(priorities, reverse=True)
    idx = 0
    length = len(priorities)
    
    for i in range(len(sorted_priorities)):   
        for j in range(len(priorities)):          
            if priorities[idx] == sorted_priorities[i]:
                if idx == location:
                    return i + 1
                else:
                    priorities[idx] = 0
                    idx = (idx + 1) % length
                    break
            idx = (idx + 1) % length


