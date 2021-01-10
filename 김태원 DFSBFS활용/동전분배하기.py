#동전분배하기
def dfs(x,a,b,c):
  global res
  if x==n:
    if a==b or a==c or b==c:
      return
    tmp=[a,b,c]    
    k=max(tmp)-min(tmp)
    if k<res:
      res=k    
  else:
    dfs(x+1,a+coin[x],b,c)
    dfs(x+1,a,b+coin[x],c)
    dfs(x+1,a,b,c+coin[x])
n=int(input())
coin=[]
res=2147000000
for i in range(n):
  tmp=int(input())
  coin.append(tmp)
dfs(0,0,0,0)
print(res)