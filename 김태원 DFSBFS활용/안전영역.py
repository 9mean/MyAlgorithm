#안전영역
from collections import deque
n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
q=deque()
big=-2147000000
small=2147000000
for i in range(n):
  for j in range(n):
    if m[i][j]>big:
      big=m[i][j]
    if m[i][j]<small:
      small=m[i][j]
cnt=0
res=0
dx=[-1,0,1,0]
dy=[0,-1,0,1]

for water in range(small-1,big):
  cnt=0
  v=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if m[i][j]>water and v[i][j]==0:
        q.append((i,j))
        v[i][j]=1
        cnt+=1
        while q:
          tmp=q.popleft()
          for k in range(4):
            x=tmp[0]+dx[k]
            y=tmp[1]+dy[k]
            if 0<=x<=n-1 and 0<=y<=n-1 and m[x][y]>water and v[x][y]==0:
              v[x][y]=1
              q.append((x,y))
  if res<cnt:
    res=cnt
print(res)