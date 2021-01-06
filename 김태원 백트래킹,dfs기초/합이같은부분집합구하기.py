#합이같은부분집합(DFS)
def dfs(x):
  global flag
  if flag==1:
    return
  if x==n:
    ls=0
    rs=0
    for i in range(n):
      if check[i]==1:
        ls+=a[i]
      else:
        rs+=a[i]
    if ls==rs:
      flag=1
      print("YES")
    return
  check[x]=1
  dfs(x+1)
  check[x]=0
  dfs(x+1)
  
n=int(input())
a=list(map(int,input().split()))
check=[0]*n
flag=0
dfs(0)
if flag==0:
  print("NO")