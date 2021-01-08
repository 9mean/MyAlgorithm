#수들의 조합
def dfs(x,hap,idx):
  global cnt
  if x==k:
    if hap%m==0:
      cnt+=1
    return
  else:
    for i in range(idx,n):
      dfs(x+1,hap+number[i],i+1)
n,k=map(int,input().split())
number=list(map(int,input().split()))
number.sort()
m=int(input())
cnt=0
dfs(0,0,0)
print(cnt)