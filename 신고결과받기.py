from collections import defaultdict

def solution(id_list, report, k):
  report_set_list = defaultdict(set)
  reported_set_list = defaultdict(set)
  for report_log in report:
    from_id, to_id = report_log.split(" ")
    report_set_list[from_id].add(to_id)
    reported_set_list[to_id].add(from_id)
    
  result = []
  for id in id_list:
    report_count = 0 
    for reported_id in report_set_list[id]:
      if len(reported_set_list[reported_id]) >= k:
        report_count += 1
    result.append(report_count)
  return result

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))