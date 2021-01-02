#봉우리
n=int(input())
m=[[0]+list(map(int,input().split()))+[0] for _ in range(n)]
m.insert(0,[0]*(n+2))
m.append([0]*(n+2))
res=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(1,n+1):
  for j in range(1,n+1):
    cnt=0
    for k in range(4):
      x=j+dx[k]
      y=i+dy[k]
      if m[i][j]>m[y][x]:
        cnt+=1
    if cnt==4:
      res+=1
print(res)