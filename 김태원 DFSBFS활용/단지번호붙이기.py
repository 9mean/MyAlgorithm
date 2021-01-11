#단지번호붙이기(DFS)
def dfs(x,y):
  global hcnt
  for i in range(4):
    fx=x+dx[i]
    fy=y+dy[i]
    if fx<0 or fx>n-1 or fy<0 or fy>n-1:
      continue
    if house[fx][fy]==0 or v[fx][fy]==1:
      continue
    if rv[fx][fy]==0:
      rv[fx][fy]=1
      hcnt+=1
    v[fx][fy]=1
    dfs(fx,fy)

n=int(input())
house=[list(map(int,input())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
v=[[0]*n for _ in range(n)]
rv=[[0]*n for _ in range(n)]
cnt=0
res=[]
for i in range(n):
  for j in range(n):
    if rv[i][j]==0:
      hcnt=0 
      dfs(i,j)
      if hcnt>0:
        cnt+=1
        res.append(hcnt)
print(cnt)
res.sort()
for i in res:
  print(i)
