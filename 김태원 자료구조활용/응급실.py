#응급실
from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=deque(a)
cnt=0
flag=0
while a:
  flag=0
  lt=a.popleft()
  for i in a:
    if lt<i:
      a.append(lt)
      flag=1
      break
  #뒤로밀렸다면
  if flag==1:
    if m==0:
      m=len(a)
  #아무런 일이없었다면
  else:
    cnt+=1
    if m==0:
      print(cnt)
      break    
  m-=1