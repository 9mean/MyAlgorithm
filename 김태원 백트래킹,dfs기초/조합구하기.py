#조합구하기
def dfs(x,s):
  global cnt
  if s>n:
    return
  if x>m-1:
    for i in res:
      print(i,end=" ")
    print()
    cnt+=1
    return
  else:
    for i in range(s,n+1):
      if check[i]==0:
        res[x]=i
        check[i]=1
        dfs(x+1,i)
        check[i]=0
n,m=map(int,input().split())
cnt=0
check=[0]*(n+1)
res=[0]*(m)
a=[0]*m
dfs(0,1)
print(cnt)
