#수들의 합
n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
left,right=0,1
while left<=right:
  tol=sum(a[left:right])
  if tol>m:
    left+=1
  elif tol==m:
    cnt+=1
    left+=1
  else :
    if right==n:
      left+=1
      continue
    right+=1
    
print(cnt)
