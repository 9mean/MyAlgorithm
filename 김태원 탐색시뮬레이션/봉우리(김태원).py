#봉우리
n=int(input())
m=[[0]+list(map(int,input().split()))+[0] for _ in range(n)]
m.insert(0,[0]*(n+2))
m.append([0]*(n+2))
cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(1,n+1):
  for j in range(1,n+1):
    if all(m[i][j]>m[i+dx[k]][j+dy[k]] for k in range(4)):
      cnt+=1
print(cnt)