#사다리타기
def dfs(x,y,start):
  global res
  flag=0
  if ladder[x][y]==2:
    res=start
  else:
    for i in range(3):
      lx=x+dx[i]
      ly=y+dy[i]
      if 0<=lx<=9 and 0<=ly<=9:
        if (i==0 or i==1) and ladder[lx][ly]==1 and v[lx][ly]==0:
          flag=1
          v[lx][ly]=1
          dfs(lx,ly,start)
        elif flag==0 and i==2 and (ladder[lx][ly]==1 or ladder[lx][ly]==2) and v[lx][ly]==0:
          v[lx][ly]=1
          dfs(lx,ly,start)
ladder=[list(map(int,input().split())) for _ in range(10)]
dx=[0,0,1]
dy=[-1,1,0]

res=0
for j in range(10):
  if res!=0:
    break
  if ladder[0][j]==1:
    v=[[0]*10 for _ in range(10)]
    v[0][j]=1
    dfs(0,j,j)
print(res)