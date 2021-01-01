#소수(에라토스테네스 체)
n=int(input())
a=[0]*(n+1)
cnt=0
for i in range(2,n+1):
  if a[i]==0:
    cnt+=1
    k=1
    while True:
      if(i*k>n):
        break
      a[i*k]=1
      k+=1
print(cnt)