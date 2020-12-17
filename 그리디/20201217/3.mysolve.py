#모험가길드
n=int(input())
people=list(map(int,input().split()))
cnt=0
people.sort()
i=0

while True:
  #인덱스초과
  if(i+people[i]-1>n-1):break

  if(people[i]==people[i+people[i]-1]) :
    cnt+=1
    i+=people[i]
  else:
    break
print(cnt)