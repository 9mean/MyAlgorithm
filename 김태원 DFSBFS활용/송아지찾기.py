#송아지찾기
from collections import deque
s,e=map(int,input().split())
v=[0]*10001
q=deque()
q.append(s)
v[s]=1
while q:
  k=q.popleft()
  if k==e:
    print(v[k]-1)
    break
  elif k-1>=0 and k+5<=10000:
    if v[k-1]==0:
      q.append(k-1)
      v[k-1]=v[k]+1
    if v[k+1]==0:
      q.append(k+1)
      v[k+1]=v[k]+1
    if v[k+5]==0:
      q.append(k+5)
      v[k+5]=v[k]+1