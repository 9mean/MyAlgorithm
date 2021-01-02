#격자판 최대합
n=int(input())
a=[]
for i in range(n):
  b=list(map(int,input().split()))
  a.append(b)
res=[]
cleft=cright=0
for i in range(n):
  row=col=0
  for j in range(n):
    row+=a[i][j]
    col+=a[j][i]
    if i==j:
      cleft+=a[i][j]
    elif i+j==n-1:
      cright+=a[i][j]
  res.append(row)
  res.append(col)
res.append(cleft)
res.append(cright)
res.sort(reverse=True)
print(res[0])