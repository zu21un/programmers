def solution(numbers, target):
    answer = 0
    stack = [0]
    for number in numbers:
        arr = []
        while len(stack) > 0:
            n = stack.pop()
            arr.append(n + number)
            arr.append(n - number)
        stack = arr
    return stack.count(target)