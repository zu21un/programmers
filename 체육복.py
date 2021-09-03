both = list(set(lost) & set(reserve))
lost = list(set(lost) - set(both))
reserve = list(set(reserve) - set(both))


answer = n - len(lost)
for p in lost:
    if p - 1 in reserve:
        answer += 1
    elif p + 1 in reserve:
        answer += 1
        reserve.remove(p + 1)
print(answer)