#도전과제(계단오르기 메모이제이션)
def dfs(x):
  if d[x]!=0:
    return d[x]
  if x==1 or x==2:
    return x
  else:
    d[x]=dfs(x-1)+dfs(x-2)
    return d[x]

n=int(input())
d=[0]*(n+1)
d[1]=1
d[2]=2
print(dfs(n))