#미로의최단거리통로
from collections import deque
road=[list(map(int,input().split())) for _ in range(7)]
q=deque()
q.append((0,0))
dx=[-1,0,1,0]
dy=[0,-1,0,1]
flag=0
while q:
  tmpx,tmpy=q.popleft()
  if tmpx==6 and tmpy==6:
    print(road[tmpx][tmpy])
    flag=1
    break
  for i in range(4):
    x=tmpx+dx[i]
    y=tmpy+dy[i]
    if x < 0 or x>6 or y<0 or y>6:
      continue
    if road[x][y]==0:
      q.append((x,y))
      road[x][y]=road[tmpx][tmpy]+1
if flag==0:
  print(-1)
