import math

def solution(n, k):
  def is_prime(num):
    if num <= 1:
      return False
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
    return True
    
  def convert(num, digit):
    if num == 0:
      return ''
    q, r = divmod(num, digit)
    return convert(q, digit) + f'{r}'
  
  convert_number = convert(n, k)
  number_list = list(convert_number.split('0'))
  result = 0
  for number in number_list:
    if len(number) == 0:
      continue
    number = int(number)
    if is_prime(number):
      result += 1
      
  return result
    
    
  
print(solution(437674,3))
print(solution(110011,10))