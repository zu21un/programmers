from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    front, end = 0, bridge_length - 1
    sum = 0
    i = 0
    while i < len(truck_weights):
        sum -= queue[front]
        front += 1
        if sum + truck_weights[i] <= weight:
            queue.append(truck_weights[i])
            sum += truck_weights[i]
            i += 1
        else:
            queue.append(0)
    return len(queue)

print(solution(2, 10, [7,4,5,6]))