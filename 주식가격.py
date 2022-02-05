def solution(prices):
    answer = [0] * len(prices)
    stack = []
    len_prices = len(prices)
    for i, v in enumerate(prices):
        p = [i, v]
        while len(stack) != 0 and p[1] < stack[-1][1]:
            p_ = stack.pop()
            answer[p_[0]] = p[0] - p_[0]
        stack.append(p)
    
    for i, v in stack:
        answer[i] = len_prices - i - 1
        
    print(answer)
    return answer

solution([1,2,3,2,3])