#사과나무
from collections import deque
n=int(input())
farm=[]
v=[[0]*(n) for _ in range(n)]
for _ in range(n):
  tmp=list(map(int,input().split()))
  farm.append(tmp)
cnt=0
q=deque()
k=[n//2,n//2]
q.append(k)
v[n//2][n//2]=1
while q:
  x,y=q.popleft()
  cnt+=farm[x][y]
  for i in (x-1,x+1,y-1,y+1):
    if i>=1 and i<=n-2:
      if i==x-1 and v[i][y]==0:
        k=[i,y]
        q.append(k)
        v[i][y]=1
      elif i==x+1 and v[i][y]==0:
        k=[i,y]
        q.append(k)
        v[i][y]=1
      elif i==y-1 and v[x][i]==0:
        k=[x,i]
        q.append(k)
        v[x][i]=1
      elif i==y+1 and v[x][i]==0:
        k=[x,i]
        q.append(k)
        v[x][i]=1
cnt+=farm[0][n//2]+farm[n//2][n-1]+farm[n//2][0]+farm[n-1][n//2]
print(cnt)
