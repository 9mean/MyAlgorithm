#수열추측하기
def dfs(x):
  global flag
  if flag==1:
    return
  if x==n:
    sum=res[0]+res[n-1]
    for i in range(1,n-1):
      sum+=s[i]*res[i]
    if sum==f:
      flag=1
      for i in res:
        print(i,end=" ")
    return
        
  else:
    for i in range(1,n+1):
      if check[i]==0:
        check[i]=1
        res[x]=i
        dfs(x+1)
        check[i]=0
flag=0
n,f=map(int,input().split())
res=[0]*n
s=[1]*n
check=[0]*(n+1)
for i in range(1,n):
  s[i]=s[i-1]*(n-i)//i
dfs(0)