from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    dp = [float('inf') for i in range(n + 1)]
    stack = [1]
    dp[1] = 0
    while stack:
        current_edge = stack.pop()
        current_dist = dp[current_edge]
        next_edges = graph[current_edge]
        for edge in next_edges:
            if current_dist + 1 < dp[edge]:
                dp[edge] = current_dist + 1
                stack.append(edge)
    return dp.count(max(dp[1:]))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
