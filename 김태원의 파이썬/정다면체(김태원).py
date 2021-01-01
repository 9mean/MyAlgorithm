n=int(input())
score=list(map(int,input().split()))
avg=round(sum(score)/n)
min=2147000000
for idx,x in enumerate(score):
  tmp=abs(x-avg)
  if tmp<min:
    min=tmp
    key=x
    ans=idx+1
  elif tmp==min:
    if x>key:
      key=x
      ans=idx+1

print(avg,ans)