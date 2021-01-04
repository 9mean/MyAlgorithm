#침몰하는타이타닉
n,m=map(int,input().split())
p=list(map(int,input().split()))
p.sort(reverse=True)
lt,rt=0,n-1
#10 9 7 6 5
cnt=0

while lt<=rt:
  k=p[lt]
  flag=0
  while True:
    if k+p[rt]<=m and flag==0:
      k+=p[rt]
      rt-=1
      flag+=1
    else:
      break
  lt+=1
  cnt+=1
print(cnt)