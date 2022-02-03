def solution(citations):
    cites = sorted(citations, reverse=True)
    h = -1
    for i, v in enumerate(cites):
        idx = i + 1
        if v > idx:
            continue
        else:
            if v == idx:
                h = idx
            elif v < idx:
                h = idx - 1
            return h
    return len(cites)