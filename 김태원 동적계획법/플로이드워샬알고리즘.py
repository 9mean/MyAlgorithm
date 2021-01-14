#플로이드워샬알고리즘 
n,m=map(int,input().split())
max=2147000
city=[[max]*n for _ in range(n)]
d=[[max]*n for _ in range(n)]
for i in range(m):
  start,end,w=map(int,input().split())
  d[start-1][end-1]=w
for i in range(n):
  d[i][i]=0
for k in range(n):
  for i in range(n):
    for j in range(n):
      if d[i][k]!=max and d[k][j]!=max:
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(n):
  for j in range(n):
    if d[i][j]==max:
      print("M",end=" ")
    else:
      print(d[i][j],end=" ")
  print()