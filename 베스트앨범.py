import collections

def solution(genres, plays):
    answer = []
    
    all_playings = collections.defaultdict(int)
    genres_to_play = collections.defaultdict(list)
    
    num = 0
    for g, p in zip(genres, plays):
        all_playings[g] += p
        genres_to_play[g].append((p, num))
        num += 1
    
    # print(genres_to_play)
    
    all_playings = sorted(all_playings.items(), key=lambda x: x[1], reverse=True)
    # print(all_playings)
    
    for g, p in all_playings:
        g_to_p = sorted(genres_to_play[g], key=lambda x: (-x[0], x[1]))[:2]
                    
        for played, idx in g_to_p:
            answer.append(idx)
    
    
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
