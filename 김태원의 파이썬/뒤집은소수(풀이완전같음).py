#뒤집은소수
def reverse(x):
  k=0
  while x!=0:
    k=10*k+x%10
    x=x//10
  return k
def isPrime(x):
  if x==1:
    return 0
  for i in range(2,x):
    if x%i==0:
      return 0
  return 1

n=int(input())
a=list(map(int,input().split()))

for i in a:
  k=reverse(i)
  if isPrime(k):
    print(k,end=" ")