#곶감
n=int(input())
gam=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
  a,b,c=map(int,input().split())
  res=[]
  if b==0:
    if c<=n:
      gam[a-1]=gam[a-1][c:]+gam[a-1][0:c]
    else:
      tmp=c%n
      gam[a-1]=gam[a-1][tmp:]+gam[a-1][0:tmp]
  else:
    if c<=n:
      gam[a-1]=gam[a-1][n-c:]+gam[a-1][0:n-c]
    else:
      tmp=c%n
      gam[a-1]=gam[a-1][n-tmp:]+gam[a-1][0:n-tmp]
k=0
for i in range(n):
  if i<=n//2:
    s,e=i,n-i-1
  else:
    s,e=n-i-1,i
  k+=sum(gam[i][s:e+1])
print(k)