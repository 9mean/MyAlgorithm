#미로탐색
from collections import deque
def dfs(x,y):
  global cnt
  v[x][y]=1
  if x==6 and y==6:
    cnt+=1
    return
  for i in range(4):
    fx=x+dx[i]
    fy=y+dy[i]
    if fx>6 or fx<0 or fy>6 or fy<0:
      continue
    if road[fx][fy]==0 and v[fx][fy]==0:
      dfs(fx,fy)
      v[fx][fy]=0
    
road=[list(map(int,input().split())) for _ in range(7)]
v=[[0]*7 for _ in range(7)]
q=deque()
q.append((0,0))
dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt=0
dfs(0,0)
print(cnt)
