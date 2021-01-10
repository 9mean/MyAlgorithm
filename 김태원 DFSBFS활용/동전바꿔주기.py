#동전바꿔주기
def dfs(x,tot):
  global res
  if tot>t:
    return
  if tot==t:
    res+=1
    return
  if x==k:
    return
  else:
    for i in range(coin[x][1]+1):
      dfs(x+1,tot+i*coin[x][0])

t=int(input())
k=int(input())
coin=[]
cnt=0
res=0
for i in range(k):
  tmp=list(map(int,input().split()))
  coin.append(tmp)
coin.sort(reverse=True)
dfs(0,0)
print(res)
