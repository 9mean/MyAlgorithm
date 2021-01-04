#증가하는수열만들기
from collections import deque
n=int(input())
a=list(map(int,input().split()))
cnt=0
res=""
a=deque(a)
k=0
while a:
  if (a[0]<k and a[-1]<k):
    break
  if len(a)==1:
    res+="L"
    cnt+=1
    break
  if a[0]<a[-1]:
    if a[0]>=k:
      k=a[0]
      a.popleft()
      res+="L"
    elif a[-1]>=k:
      k=a[-1]
      a.pop()
      res+="R"
  else:
    if a[-1]>=k:
      k=a[-1]
      a.pop()
      res+="R"
    elif a[0]>=k:
      k=a[0]
      a.popleft()
      res+="L"
  cnt+=1
print(cnt)
print(res)