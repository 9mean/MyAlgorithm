#순열구하기
def dfs(x,res):
  global cnt
  global check
  if x==m:
    print(res) 
    cnt+=1
    return
  else:
    for i in range(1,n+1):
      if check[i]==0:
        check[i]=1
        dfs(x+1,res+str(i))
        check[i]=0
n,m=map(int,input().split())
check=[0]*(n+1)
cnt=0
res=""
dfs(0,res)
print(cnt)
