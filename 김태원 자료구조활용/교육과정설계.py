#교육과정설계
from collections import deque
plan=list(input())
n=int(input())
for i in range(n):
  k=[]
  a=list(input())
  a=deque(a)
  while a:
    tmp=a.popleft()
    if tmp in plan and tmp not in k:
      k.append(tmp)
  if k==plan:
    print("#%d YES"%(i+1))
  else:
    print("#%d NO"%(i+1))
