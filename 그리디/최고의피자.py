n=int(input())
a,b=map(int,input().split())
douc=int(input())
topc=[]
for _ in range(n):
  i=int(input())
  topc.append(i)

topc.sort(reverse=True)
result=0
tmp=0
cnt=0
for i in topc:
  cnt+=1
  tmp+=i
  k=(douc+tmp)/(a+b*cnt)
  result=max(result,k)

print(int(result))