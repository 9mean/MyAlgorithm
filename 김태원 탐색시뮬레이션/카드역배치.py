#카드 역배치
k=[1]*20
for i in range(20):
  k[i]=i+1
for i in range(10):
  a,b=map(int,input().split())
  left=a-1
  right=b-1
  while left<right:
    tmp=k[right]
    k[right]=k[left]
    k[left]=tmp
    left+=1
    right-=1
for i in k:
  print(i,end=" ")