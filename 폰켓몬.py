def solution(nums):
	nums_except_duplicates = set(nums)
	return min(int(len(nums) / 2), len(nums_except_duplicates))
0
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
  
  