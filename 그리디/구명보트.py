people=[7,8,5]
limit=10
answer = 0
people.sort(reverse=True)
#80 70 50 50
for i in range(len(people)):
  #현재선택한값이 제한-현잿값이 최솟값보다 크다면 탐색하고 아니라면 다음애로 넘어가
  # if limit-i < people[len(people)-1]:
    
  #   print("처음삭제")
  #   people.remove(i)
  #   answer+=1
  cnt=0
  for j in range(len(people)):
    cnt+=1
    #현재사람과 그다음으로 보트를 최대한 꽉채우는 사람이 발견되면 태우기
    if people[i]+people[j] <= limit:
      answer+=1
      people.remove(people[i])
      jdx=people.index(people[j])
      people.remove(people[jdx])
      break
    #발견하지 못하면 현재사람만 태우기
    if cnt==len(people):
      answer+=1
      people.remove(people[i])
    
print(answer)