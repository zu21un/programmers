def solution(clothes):
    answer = 1
    ls = {}
    for c in clothes:
        category = c[1]
        if category in ls:
            ls[category] += 1
        else:
            ls[category] = 1
            
    for v in ls.values():
        answer *= (v + 1)
    answer -= 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))