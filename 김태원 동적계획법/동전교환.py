#동전교환
n=int(input())
coin=list(map(int,input().split()))
coin.sort()
m=int(input())
d=[0]*(m+1)
for i in range(n):
  for j in range(coin[i],m+1):
    if j%coin[i]==0:
      d[j]=j//coin[i]
    else:
      d[j]=min(d[j],d[j-coin[i]]+1)
print(d[m])