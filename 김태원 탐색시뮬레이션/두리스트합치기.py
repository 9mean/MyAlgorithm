#두 리스트 합치기
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

pa,pb,idx=0,0,0
c=[0]*(n+m)
while pa!=n and pb!=m:
  if a[pa]<=b[pb]:
    c[idx]=a[pa]
    pa+=1
  else:
    c[idx]=b[pb]
    pb+=1
  idx+=1
if pa==n:
  c[idx:idx+m-pb]=b[pb:m]
else:
  c[idx:idx+m-pa]=a[pa:n]
for i in c:
  print(i,end=" ")