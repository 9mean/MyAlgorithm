#양팔저울(시간초과)
def dfs(ls,rs,idx):
  global res
  if i+ls==rs:
    res.add(i)
    return
  if idx==k:
    return
  else:
    dfs(ls+chu[idx],rs,idx+1)
    dfs(ls,rs+chu[idx],idx+1)
    dfs(ls,rs,idx+1)
res=set()
k=int(input())
chu=list(map(int,input().split()))
s=sum(chu)
for i in range(1,s+1):
  dfs(0,0,0)
print(s-len(res))