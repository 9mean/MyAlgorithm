from collections import deque
def bfs(x,y):
  q=deque()
  q.append((x,y))
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if ice[nx][ny]==0:
        continue
      if ice[nx][ny]==1:
        ice[nx][ny]=ice[x][y]+1
        q.append((nx,ny))
  return ice[n-1][m-1]
    

n,m=list(map(int,input().split()))

ice=[]
for i in range(n):
  ice.append(list(map(int,input())))
#bfs
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))
