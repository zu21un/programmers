def solution(citations):
    cites = sorted(citations, reverse=True)
    h = -1
    for i, v in enumerate(cites, start = 1):
        if v > i:
            continue
        else:
            if v == i:
                h = i
            elif v < i:
                h = i - 1
            return h
    return len(cites)