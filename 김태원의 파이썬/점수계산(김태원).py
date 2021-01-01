#주사위게임
n=int(input())
res=0
for i in range(n):
  tmp=input().split()
  tmp.sort()
  a,b,c=map(int,tmp)
  if a==b and b==c and a==c:
    sum=10000+a*1000
  elif a==b or a==c:
    sum=1000+(a*100)
  elif b==c:
    sum=1000+(b*100)
  else:
    sum=c*100
  if sum>res:
    res=sum
print(sum)

