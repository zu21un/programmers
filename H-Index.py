def solution(citations):
    cites = sorted(citations, reverse=True)
    for i, v in enumerate(cites, start = 1):
        if v > i:
            continue
        else:
            if v == i:
                return i
            elif v < i:
                return i - 1
    return len(cites)