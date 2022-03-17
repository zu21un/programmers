from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append((begin, []))
    while queue:
        current_word, changed = queue.popleft()
        if current_word == target:
            return len(changed)
        else:
            for idx, word in enumerate(words):
                diff_count = 0
                for i in range(0, len(word)):
                    if current_word[i] != word[i]:
                        diff_count += 1
                if diff_count == 1 and idx not in changed:
                    new_changed = changed[:]
                    new_changed.append(idx)
                    queue.append((word, new_changed))
                    
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]	))