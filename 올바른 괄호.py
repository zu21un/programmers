def solution(s):
    answer = True
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) == 0 or stack[-1] == ')':
                answer = False
                break
            else:
                stack.pop()
    return answer