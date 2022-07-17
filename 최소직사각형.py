def solution(sizes):
    max_width = max_height = - 1
    for width, height in sizes:
        longer, shorter = max(width, height), min(width, height)
        max_width = max(max_width, longer)
        max_height = max(max_height, shorter)

    return max_width * max_height