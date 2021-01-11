#등산경로
def dfs(x,y):
  global cnt
  if x==goalx and y==goaly:
    cnt+=1
    return
  for i in range(4):
    fx=x+dx[i]
    fy=y+dy[i]
    if fx>n-1 or fx<0 or fy>n-1 or fy<0:
      continue
    if road[fx][fy]>road[x][y]:
      dfs(fx,fy)
    
n=int(input())
road=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt=0

startx,starty=0,0
goalx,goaly=0,0
start=2147000000
goal=0
for i in range(n):
  for j in range(n):
    if road[i][j]>goal:
      goal=road[i][j]
      goalx,goaly=i,j 
    if road[i][j]<start:
      start=road[i][j]
      startx,starty=i,j
dfs(startx,starty)   
print(cnt)
