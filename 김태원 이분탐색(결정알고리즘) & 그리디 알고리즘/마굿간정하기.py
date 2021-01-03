#마구간
def Count(x):
  cnt=0
  idx=m[0]
  for i in range(1,n):
    if m[i]-idx >= x:
      cnt+=1
      idx=m[i]
  return cnt+1

n,c=map(int,input().split())
m=[]
for i in range(n):
  tmp=int(input())
  m.append(tmp)
m.sort()
left,right=1,m[n-1]
while left<=right:
  mid=(left+right)//2
  if Count(mid)>=c:
    left=mid+1
    res=mid
  else:
    right=mid-1
print(res)