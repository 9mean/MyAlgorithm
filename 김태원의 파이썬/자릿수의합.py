#자릿수의 합
def digit_sum(x):
  a=0
  while x!=0:
    k=x%10
    x=x//10
    a+=k
  return a
n=int(input())
a=list(map(int,input().split()))
max=digit_sum(a[0])
idx=0
for i in range(n):
  tmp=digit_sum(a[i])
  if max<tmp:
    max=tmp
    idx=i
print(a[idx])