#카드 역배치
k=list(range(1,21))
for _ in range(10):
  a,b=map(int,input().split())
  for i in range((b-a+1)//2):
    k[a+i],k[b-i]=k[b-1],k[a+i]

k.pop(0)
for x in a:
  print(x,end=" ")