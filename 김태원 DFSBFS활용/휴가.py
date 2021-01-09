#휴가
def dfs(x,benefit):
  global res
  if x>n:
    return
  if x==n:
    if benefit>res:
      res=benefit
  else:
    dfs(x+a[x][0],benefit+a[x][1])
    dfs(x+1,benefit)
n=int(input())
a=[]
for _ in range(n):
  tmp=list(map(int,input().split()))
  a.append(tmp)
res=-2147000000
dfs(0,0)
print(res)