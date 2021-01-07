#중복순열구하기
def dfs(l,res):
  global cnt
  if l==m-1:
    print(res)
    cnt+=1
    return
  else:
    for i in range(1,n+1):
      dfs(l+1,res+str(i))
    
    
n,m=map(int,input().split())
res=""
cnt=0
for i in range(1,n+1):
  dfs(0,res+str(i))
print(cnt)

  