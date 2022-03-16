from collections import defaultdict

def solution(N, number):
    if N == number:
        return 1
    
    count_to_num = defaultdict(set)
    
    n = 0
    for i in range(1, 9):
        n += N
        count_to_num[i].add(n)
        n *= 10
    for i in range(2, 9):
        for j in range(1, i):
            for num1 in count_to_num[j]:
                for num2 in count_to_num[i - j]:
                    count_to_num[i].add(num1 + num2)
                    count_to_num[i].add(num1 * num2)
                    count_to_num[i].add(num1 - num2)
                    if num2 != 0:
                        count_to_num[i].add(num1 // num2)
        if number in count_to_num[i]:
            return i
                        
    return -1

print(solution(2,11))