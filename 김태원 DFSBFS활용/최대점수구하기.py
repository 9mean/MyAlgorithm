#최대점수 구하기
def dfs(x,cur,time):
  global res
  if time>m:
    return
  if cur>res:
    res=cur
  for i in range(x,n):
    dfs(i+1,cur+s[i][0],time+s[i][1])
n,m=map(int,input().split())
s=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  s.append(tmp)
res=-2147000000
dfs(0,0,0)
print(res)