#랜선자르기(결정알고리즘)
k,n=map(int,input().split())
a=[]
for i in range(k):
  tmp=int(input())
  a.append(tmp)

right=max(a)
left=0
while left<=right:
  mid=(left+right)//2
  cnt=0
  for i in a:
    cnt+=i//mid
  if cnt<n:
    right=mid-1
  elif cnt>=n:
    left=mid+1
print(left-1)

