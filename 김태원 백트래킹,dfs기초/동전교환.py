#동전교환
def dfs(v,total,cnt):
  global res
  if total==m:
    if res>cnt:
      res=cnt
    return
  if total>m or cnt>res:
    return
  for i in range(n-1,-1,-1):
    dfs(i,total+coin[i],cnt+1)

n=int(input())
coin=list(map(int,input().split()))
m=int(input())
res=217000000
dfs(n-1,0,0)
print(res)
