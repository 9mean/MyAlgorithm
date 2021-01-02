#두 리스트 합치기
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

pa,pb,idx=0,0,0
c=[]
while pa<n and pb<m:
  if a[pa]<=b[pb]:
    c.append(a[pa])
    pa+=1
  else:
    c.append(b[pb])
    pb+=1
if pa<n:
  c=c+a[pa:]
else:
  c=c+b[pb:]
for i in c:
  print(i,end=" ")