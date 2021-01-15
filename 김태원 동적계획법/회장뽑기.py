#회장뽑기
n=int(input())
p=[[100]*n for _ in range(n)]
while True:
  l,r=map(int,input().split())
  if l==-1 and r==-1:
    break
  p[l-1][r-1]=1
  p[r-1][l-1]=1
for i in range(n):
  p[i][i]=0
res=[]
for k in range(n):
  key=0
  for i in range(n):
    for j in range(n):
      p[i][j]=min(p[i][j],p[i][k]+p[k][j])

for i in range(n):
  res.append(max(p[i]))
key=min(res)
cnt=0
for i in range(n):
  if res[i]==key:
    cnt+=1
print(key,cnt)
for i in range(n):
  if res[i]==key:
    print(i+1,end=" ")