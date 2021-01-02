#격자판 최대합
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

large=-2147000000
for i in range(n):
  sum1=sum2=0
  for j in range(n):
    sum1+=a[i][j]
    sum2+=a[j][i]
  if sum1>large:
    large=sum1
  if sum2>large:
    large=sum2

sum1=sum2=0
for i in range(n):
  sum1+=a[i][i]
  sum2+=a[i][n-i-1]
if sum1>large:
  large=sum1
if sum2>large:
  large=sum2
print(large)