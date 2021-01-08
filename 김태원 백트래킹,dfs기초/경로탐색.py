#경로탐색
def dfs(vertext):
  global cnt
  visit[vertext]=1
  if vertext==n:
    cnt+=1
  else:
    for i in range(1,n+1):
      if visit[i]==0 and v[vertext][i]==1:
        dfs(i)
        visit[i]=0
n,m=map(int,input().split())
v=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(m):
  s,e=map(int,input().split())
  v[s][e]=1

cnt=0
dfs(1)
print(cnt)
