#최대힙
import heapq as hq
a=[]
while True:
  n=int(input())
  if n==-1:
    break
  if n==0:
    if len(a)==0:
      print(-1)
    else:
      k=-hq.heappop(a)
      print(k)
  else:
    hq.heappush(a,-n)