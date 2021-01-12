#도전과제(돌다리 건너기 바텀업)
n=int(input())
d=[0]*(n+2)
d[1]=1
d[2]=2
for i in range(3,n+2):
  d[i]=d[i-1]+d[i-2]
print(d[n+1])