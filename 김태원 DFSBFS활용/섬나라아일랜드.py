#섬나라아일랜드
from collections import deque
n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
q=deque()
dx=[-1,0,1,0,1,1,-1,-1]
dy=[0,-1,0,1,-1,1,1,-1]
cnt=0
for i in range(n):
  for j in range(n):
    if m[i][j]==1:
      m[i][j]=0
      q.append((i,j))
      while q:
        kx,ky=q.popleft()
        for k in range(8):
          bx=kx+dx[k]
          by=ky+dy[k]
          if 0<=bx<=n-1 and 0<=by<=n-1:
            if m[bx][by]==1:
              q.append((bx,by))
              m[bx][by]=0
      cnt+=1
print(cnt)