#정다면체
n,m=map(int,input().split())
ans=[0 * 0 for _ in range(33)]

for i in range(1,n+1):
  for j in range(1,m+1):
    sum=i+j
    ans[sum]+=1
key=max(ans)
for i in range(33):
  if key==ans[i]:
    print(i,end=" ")
