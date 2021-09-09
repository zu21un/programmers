def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score_one = 0
    score_two = 0
    score_three = 0
    idx_one = 0
    idx_two = 0
    idx_three = 0
    winner = []
    for answer in answers:
        if one[idx_one] == answer:
            score_one += 1
        if two[idx_two] == answer:
            score_two += 1
        if three[idx_three] == answer:
            score_three += 1
        idx_one += 1
        idx_two += 1
        idx_three += 1
        if idx_one >= len(one):
            idx_one %= len(one)
        if idx_two >= len(two):
            idx_two %= len(two)
        if idx_three >= len(three):
            idx_three %= len(three)
    max_score = max(score_one, score_two, score_three)
    if max_score == score_one:
        winner.append(1)
    if max_score == score_two:
        winner.append(2)
    if max_score == score_three:
        winner.append(3)
    return winner
