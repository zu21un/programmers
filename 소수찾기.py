import math
from itertools import permutations

def solution(numbers):
    answer = []
    max_number = int(''.join(sorted(numbers, reverse=True)))
    
    err = [True for _ in range(max_number + 1)]

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(max_number)) + 1):
        if err[i] == True:
            j = 2
            while i * j <= max_number:
                err[i * j] = False
                j += 1
                
    numbers_list = list(numbers)
    
    for i in range(1, len(numbers) + 1):
        ls = list(permutations(numbers_list, i))
        
        for num in ls:
            num = int(''.join(num))
            if num >= 2 and err[num] == True:
                answer.append(num)

    return len(set(answer))

print(solution("011"))