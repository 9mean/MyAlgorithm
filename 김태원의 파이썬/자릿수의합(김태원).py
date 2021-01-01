#자릿수의 합
def digit_sum(x):
  sum=0
  for i in str(x):
    sum+=int(i)
  return sum 
n=int(input())
a=list(map(int,input().split()))
max=digit_sum(a[0])
idx=0
for i in a:
  tmp=digit_sum(i)
  if max<tmp:
    max=tmp
    res=i
print(res)