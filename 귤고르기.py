from collections import Counter

def solution(k, tangerine):
  counted_tangerine = Counter(tangerine).most_common()
  
  result = answer = 0
  
  for size, count in counted_tangerine:
    result += count
    answer += 1
    if result >= k:
      break
  
  return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, 	[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, 	[1, 1, 1, 1, 2, 2, 2, 3]))
