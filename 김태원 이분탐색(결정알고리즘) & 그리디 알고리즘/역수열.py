#역수열
n=int(input())
r=list(map(int,input().split()))
res=[]
for i in range(n-1,-1,-1):
  res.insert(r[i],i+1)
for i in res:
  print(i,end=" ")
# 000001
# 0002
# 00003
# 4
# 005
# 06
# 07
# 8
