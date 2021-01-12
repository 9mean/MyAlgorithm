#토마토
from collections import deque
n,m=map(int,input().split())
farm=[list(map(int,input().split())) for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
cnt=0
flag=0
for i in range(m):
  for j in range(n):
    if farm[i][j]==1:
      q.append((i,j))
if len(q)==n*m:
  print(0)
  flag=2
else :
  tracx,tracy=q.pop()
  q.append((tracx,tracy))
  while q:
    tmp=q.popleft()
    if q and tmp[0]==tracx and tmp[1]==tracy:
      tracx,tracy=q.pop()
      q.append((tracx,tracy))
      cnt+=1
    for k in range(4):
      px=tmp[0]+dx[k]
      py=tmp[1]+dy[k]
      if 0<=px<=m-1 and 0<=py<=n-1 and farm[px][py]==0:
        farm[px][py]=1
        q.append((px,py))

for i in range(m):
  if flag==1:
    break
  for j in range(n):
    if farm[i][j]==0:
      print(-1)
      flag=1
      break

if flag==0 :
  print(cnt)