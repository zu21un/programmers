import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    while len(heap) >= 2:
        if heap[0] >= K:
            return answer
        else:
            smallest = heapq.heappop(heap)
            second_smallest = heapq.heappop(heap)
            mix = smallest + second_smallest * 2
            heapq.heappush(heap, mix)
            answer += 1
    if heap[0] >= K:
        return answer
    else:
        return -1