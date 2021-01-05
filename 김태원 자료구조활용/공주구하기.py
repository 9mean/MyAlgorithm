#공주구하기
from collections import deque
n,k=map(int,input().split())
a=list(i+1 for i in range(n))
q=deque(a)
while q:
  if len(q)==1:
    break
  for i in range(k-1):
    r=q.popleft()
    q.append(r)
  q.popleft()
print(q[0])