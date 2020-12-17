#기존의 내가 풀던방식은 o(n)인데
#이 방식은 o(logn)이다..최대한 빨리 줄여보자

n,k=map(int,input().split())

cnt=0

while True :
  target=(n//k)*k
  cnt+=(n-target)
  n=target
  if n<k:
    break
  cnt+=1
  n/=k
  
cnt+=(n-1)
print(int(cnt))

